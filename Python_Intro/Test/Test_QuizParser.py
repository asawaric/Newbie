import ConfigParser
import glob
from collections import OrderedDict

config = ConfigParser.ConfigParser()
for fileName in glob.glob('*.cfg'):
    config.read(fileName)
    problem_list = []
    
    for section in config.sections():
        curr_problem = {}
        choices = {}

    print "Found question named:", section
    curr_problem["name"] = section

    for opt in config.options(section):
        if opt == "statement":
            res = config.get(section, opt)
            curr_problem["question"] = res
        else:
            res = config.get(section, opt).split("::")
            choices[res[0]] = res[1]

    curr_problem.update({'choices':choices})
    problem_list.append(curr_problem)

for p in problem_list:
    print 80*"*"
    print p['question']
    print ""
    for n, (k,v) in enumerate(p['choices'].items()):
        print "%d)"%(n+1), k, "(%s)"%v
