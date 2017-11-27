import csv, json, re, os

path = '/Users/kon9654/Documents/sei_data/resumes_txt/'
tags = ['Reporting', 'Frameworks', 'Databases', 'Languages', 'Applications','Methodologies', 'Deliverables', 'Technologies', 'Functional Areas', 'Industries', 'Education', 'Certifications']


def getSkillsJSON(filename):
    sei_name = filename.split('-')[1].strip().split('_')[0]
    #print(sei_name)
    with open(filename,'rb') as f:
        skills = {}
        skills["name"] = sei_name
        skills["skills"] = {}
        reader = csv.reader(f,delimiter='\n')

        for line in reader:
            if len(line)>0:
                if any(tag in line[0] for tag in tags):
                    sline = line[0].split('\t')
                    if len(sline) > 1:
                        aline = re.split("\xe2\x80\xa2", sline[1])
                        if len(aline) == 1:
                            aline = sline[1].split(',')
                        skills["skills"][sline[0]] = aline

        return skills

def flattenJson(j):
    total = "name,type,skill,order\n"
    for i in j:
        line = i['name'] + ","
        for key in i['skills']:
            counter = 1
            for s in i['skills'][key]:
                total += line + key.strip(':') + "," + s.strip() + "," + str(counter) + "\n"
                counter+=1
    return total

sei = []
for f in os.listdir(path):
    #print "here"
    #print path+f
    sei.append(getSkillsJSON(path+f))

#print(sei)
print(flattenJson(sei))
