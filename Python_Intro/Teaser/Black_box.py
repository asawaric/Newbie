import random
from List_sums import sample_space
def Black_box(n,m):
    lst1 = sample_space(n)
    lst2 = [(random.choice(lst1)) for j in range(m)]
    print lst2
    lst3 = [(lst2.count(i)) for i  in set(lst2)]
    print lst3
    probability = [(float(i)/m) for i in lst3]
    print probability
Black_box(10,2)
