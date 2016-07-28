asimov_robot_rules = "A robot may not injure a human being or, through inaction, allow a human being to come to harm. A robot must obey orders given it by human beings except where such orders would conflict with the First Law. A robot must protect its own existence as long as such protection does not conflict with the First or Second Law.".split(' ')

lst = [l.lower().rstrip('.').rstrip(',') for l in asimov_robot_rules]

ans_dict = {}

def add_to_dict (ans_dict, word, position):
    if word in ans_dict.keys():
        ans_dict[word].append(position)
    else:
        ans_dict[word] = [position]

robot_pos = [(position, word) for position,word in enumerate(lst)]

for word in robot_pos:
     add_to_dict(ans_dict, word[1], word[0])
#print ans_dict

unsorted_counts = {key:len(value) for key, value in ans_dict.iteritems()}

#print unsorted_counts

import operator

result = sorted(unsorted_counts.items(), key=operator.itemgetter(1))

result.reverse()

print result
