divisible_by_13 = lambda x: ((x%13)==0 and (x%2)==0)
print filter(divisible_by_13, range(1,201))


multiply = lambda x,y: (x*y)
print reduce(multiply,(filter(divisible_by_13, range(1,201))))

add = lambda x,y: (x+y)
square = lambda x: x*x
a = map(square,filter(divisible_by_13, range(1,201)))
print reduce(add,a)
 
