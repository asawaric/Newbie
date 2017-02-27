import matplotlib.pyplot as plt
import pylab

results1 = []
polygon1 = []

with open('/home/asawari/Desktop/Lab/DengueData/SGof3polygons/coords1.txt') as f:
    for line in f:
        results1.append(line.strip().split('\t'))
polygon1 = [tuple(float(i) for i in j)for j in results1]
a = list(zip(*polygon1))[0]
b = list(zip(*polygon1))[1]
#plt.plot(b, a)

results2 = []
polygon2 = []
with open('/home/asawari/Desktop/Lab/DengueData/SGof3polygons/coords2.txt') as f:
    for line in f:
        results2.append(line.strip().split('\t'))
polygon2 = [tuple(float(i) for i in j)for j in results2]
c = list(zip(*polygon2))[0]
d = list(zip(*polygon2))[1]

results3 = []
polygon3 = []
with open('/home/asawari/Desktop/Lab/DengueData/SGof3polygons/coords3.txt') as f:
    for line in f:
        results3.append(line.strip().split('\t'))

polygon3 = [tuple(float(i) for i in j)for j in results3]
e = list(zip(*polygon3))[0]
f = list(zip(*polygon3))[1]

fig, ax = plt.subplots()
ax.plot(b, a, color='green')
ax.plot(d, c, color='red')
ax.plot(f, e, color='blue')
plt.title('SG of 3 Polygons')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
