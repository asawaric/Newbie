import sample_space
from sample_space import outcomes
lst_a = outcomes(6)
event_space = [sum(i) for i in lst_a]
unique_sums = set(event_space)
print unique_sums
print len(unique_sums)


