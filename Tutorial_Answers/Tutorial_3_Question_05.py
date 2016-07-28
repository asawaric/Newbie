asimov_robot_rules = "A robot may not injure a human being or, through inaction, allow a human being to come to harm. A robot must obey orders given it by human beings except where such orders would conflict with the First Law. A robot must protect its own existence as long as such protection does not conflict with the First or Second Law.".split(" ")


lst = [l.lower().rstrip('.').rstrip(',') for l in asimov_robot_rules]

print len(set(lst))

a = set(lst)

asimov_tool_rules = "A tool must not be unsafe to use. Hammers have handles and screwdrivers have hilts to help increase grip. It is of course possible for a person to injure himself with one of these tools, but that injury would only be due to his incompetence, not the design of the tool. A tool must perform its function efficiently unless this would harm the user. This is the entire reason ground-fault circuit interrupters exist. Any running tool will have its power cut if a circuit senses that some current is not returning to the neutral wire, and hence might be flowing through the user. The safety of the user is paramount. A tool must remain intact during its use unless its destruction is required for its use or for safety. For example, Dremel disks are designed to be as tough as possible without breaking unless the job requires it to be spent. Furthermore, they are designed to break at a point before the shrapnel velocity could seriously injure someone".split(' ')

lst_2 = [l.lower().rstrip('.').rstrip(',') for l in asimov_tool_rules]

b = set(lst_2)

print len(a&b)
print len(a-b)
print len(b-a)
