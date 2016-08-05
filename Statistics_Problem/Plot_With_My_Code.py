import itertools
import collections
import matplotlib.pyplot as plt    

#create the sample space and sum

lst1 = [1, 2, 3, 4, 5, 6]
lst3 = []
lst4 = []
lst5 = []
lst6 = []
def sample_space(n):
    lst2 = itertools.product(lst1,repeat=n)
    for elem in lst2:
        lst3.append(sum(elem))  
#make dictionary of occurrences and values
    occur = collections.Counter(lst3)
    
    for element in occur:
        x = occur.keys()
        y = occur.values()
        plt.scatter(x,y)
    plt.show()           
sample_space(3) 
