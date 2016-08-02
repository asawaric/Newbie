import sample_space
from sample_space import outcomes
import collections

n = 4  
lst_b = outcomes(n) 
lst1 = [sum(i) for i in lst_b] 

for j in lst1:
    lst2 = collections.Counter(lst1)  

for key, val in lst2.iteritems():
    lst3 = lst2.keys()
    lst4 = lst2.values() 
    
lst5 = [(x*y)/(6.0**n) for x,y in zip(lst3,lst4)] 

Avg_val = sum(lst5)
print lst2
print Avg_val
