# inputPath = "input_data/a_an_example.in.txt"
# inputPath = "input_data/b_better_start_small.in.txt"
# inputPath = "input_data/c_collaboration.in.txt"
# inputPath = "input_data/d_dense_schedule.in.txt"
# inputPath = "input_data/e_exceptional_skills.in.txt"
inputPath = "input_data/f_find_great_mentors.in.txt"


# ----------------------- Read Input File --------------------------
with open(inputPath) as f:
    data = f.read()
    data = data.splitlines()

contributor, project = map(int, data[0].split())


# ---------------------- Parse Contributors ------------------------
i = 1
contributors = {}
skl = {}
for _ in range(contributor):
    name, skills = data[i].split()
    contributors[name] = list()
    i += 1
    for _ in range(int(skills)):
        skill, level = data[i].split()
        contributors[name].append((skill, int(level)))
        i += 1
        sc = skl.get(skill, ("", 0))[1]
        if int(level) > sc:
            skl[skill] = (name, int(level))


# -------------------- Parse Projects ------------------------------
projects ={}
for _ in range(project):
    prjName, d, s, b, r = data[i].split()
    i += 1
    projects[prjName] = {
        'days': int(d),
        'score': int(s),
        'bestbefore': int(b),
        'numskills': int(r),
        'skill': list()
    }
    for _ in range(int(r)):
        skill, level = data[i].split()
        projects[prjName]['skill'].append((skill, int(level)))
        i += 1


# ------------------------ match skill for project -------------------
xyz = 0
fnlst = []
for name,prj in projects.items():
    skills = prj['skill']
    count = 0
    out = ""
    out += name
    out += "\n"
    contl = []
    conts = set()
    for skill, level in skills:
        if skl[skill][1] >= level:
            conts.add(skl[skill][0])
            contl.append(skl[skill][0])
            count += 1
    if count == len(skills):
        if len(conts) == len(contl):
            xyz += 1
            out += " ".join(contl)
            fnlst.append({
                'prj': name,
                'score': prj['score'],
                'con': contl
            })


# ----------------- sort projects by score ------------------
fnlst.sort(key=lambda x: x['score'], reverse=True)


# ----------------- create output file ----------------------
with open(f"output_data/{inputPath[11::].split('.')[0]}.txt", 'w') as f:
    for x in fnlst[:1000]:
        f.write(f"{x['prj']}\n{' '.join(x['con'])}\n")