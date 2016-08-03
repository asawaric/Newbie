import matplotlib.pyplot as plt
lst = [1,2,3,4,5,6]
throws = [[i] for i in lst]
n=6
for k in range(n-1):
    throws = [i + [j] for i in throws for j in lst]

lst2 = [sum(i) for i in throws]

dict1 = dict((v,lst2.count(v)) for v in set(lst2))

for elem in dict1:
    x = dict1.keys()
    y = dict1.values()

lst3 = [(i*j)/(6.0**n) for i,j in zip(x,y)]
Average_value = sum(lst3)
print Average_value

plt.plot(x,y, '8')
plt.xlabel('Sum')
plt.ylabel('Frequency of occurrence')
plt.title('Frequency Vs Sum')
plt.savefig("6_die_throws.png")
plt.show()
    
