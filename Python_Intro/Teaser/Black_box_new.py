import random
import math
def Black_box(dice,throws):
    lst1 = [[random.randint(1,6) for i in range(dice)] for i in range(throws)]
    lst2 = [sum(i) for i in lst1]
    dict1 = {v:0 for v in set(lst2)}
    for v in lst2:
        dict1[v] += 1
    probability = {v:float(dict1[v])/throws for v in dict1}
    return probability


def dice_finder(n, m):
    dict3 = {} 
    for i in range(int(math.ceil((n/6))),(n+1)):
        dict2 = Black_box(i, m)
        if n in dict2.keys():
            dict3[i] = dict2[n]
    
    print dict3

dice_finder(51,10000)
