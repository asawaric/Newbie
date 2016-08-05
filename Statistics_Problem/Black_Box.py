import random
import Expected_Value_Use
from Expected_Value_Use import sample_space_2
lst2 = []
def Black_Box(n,m):
    lst1 = sample_space_2(n)
    for m in range(m):
        lst2.append(random.choice(lst1))
    lst3 = [(lst2.count(i)) for i in set(lst2)]
    print lst3
    probability = [(float(i)/m) for i in lst3]
    print probability 
Black_Box(8,5)
