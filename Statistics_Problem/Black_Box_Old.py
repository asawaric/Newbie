import rando
import Expected_Value_Use
from Expected_Value_Use import sample_space_2

lst = [1, 2, 3, 4, 5, 6]
lst1 = []
lst2 = []

def Black_Box(n,m):
    throws = [[i] for i in lst]
    for i in range(n-1):
        throws = [[i] + j for i in lst for j in throws]
    for elem in throws:
        lst1.append(sum(elem))
    for m in range(m):
        lst2.append(random.choice(lst1))
    print lst2
    lst3 = [(lst2.count(i)) for i in set(lst2)]
    print lst3 
    probability = [(float(i)/m) for i in lst3]
    print probability 
#calculates probability for m-1
Black_Box(8,5)
