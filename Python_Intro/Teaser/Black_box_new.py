import random
def Black_box(dice,throws):
    lst1 = [list((random.choice([1,2,3,4,5,6])) for i in range(throws)) for i in range(dice)]
    lst2 = [sum(i) for i in lst1]
    dict1 = {v:0 for v in set(lst2)}
    for v in lst2:
        dict1[v] += 1
    probability = {v:float(dict1[v])/throws for v in dict1}
    print probability
Black_box(1000, 1000)

