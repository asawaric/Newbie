import collections
import matplotlib.pyplot as plt

lst1 = [1, 2, 3, 4, 5, 6]
lst2 = []

def sample_space_3(n):
    for i in range(n):
        throws = [[i] for i in lst1]    
        throws = [[i] + j for i in lst1 for j in throws]
        print throws
    for elem in throws:
        lst2.append(sum(elem))
    occur = collections.Counter(lst2)
    print occur
# for elem2 in occur:
    #    x = occur.keys()
   #     y = occur.values()
  #      plt.scatter(x,y)
 #   plt.show()
sample_space_3(4)

