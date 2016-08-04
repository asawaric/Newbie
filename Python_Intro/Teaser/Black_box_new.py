import random
def Black_box(n,m):
    lst1 = [list((random.choice([1,2,3,4,5,6])) for i in range(n)) for i in range(m)]
    lst2 = [sum(i) for i in lst1]
    dict1 = dict((v, lst2.count(v)) for v in lst2)
    probability = dict((v,(float(lst2.count(v))/m)) for v in lst2)
    print probability
Black_box(100, 100)

