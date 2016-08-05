import itertools
import collections    

#create the sample space and sum

lst1 = [1, 2, 3, 4, 5, 6]
lst3 = []
lst4 = []
lst5 = []
lst6 = []
def sample_space(n):
    lst2 = itertools.product(lst1,repeat=n):
    for elem in lst2:
        lst3.append(sum(elem))  
#make dictionary of occurrences and values
    occur = collections.Counter(lst3)
    for elem2,elem3 in occur.iteritems():
        lst5.append(elem2*elem3)
    for elem4 in lst5:
        lst6.append(elem4/(6.0**n))
    print sum(lst6)

sample_space(5)    
            
                       
