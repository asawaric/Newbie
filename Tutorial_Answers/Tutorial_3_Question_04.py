#1Consider the tuple long_tup below. Add the terms "Computation" and "9999" to this tuple

long_tup ='Physics', 'Biology', '14567', '21345', 'Chemistry', 'Mathematics', '5698', '3427'

new_long_tup = long_tup + ('Computation','9999', 'a5')
print new_long_tup

#2
# A tuple is immutable and thus can not be referenced by index

#3
#alph = [elem for elem in new_long_tup if elem.isalpha()]
#num = [elem for elem in new_long_tup if elem.isdigit()]
#print alph
#print num

alph = ()
num = ()

for elem in new_long_tup:
    if elem.isalpha() == True:
        alph= alph + (elem,)
    elif elem.isdigit() == True:
        num += (elem,)
        
print alph
print num


#4

alph = tuple([elem for elem in new_long_tup if elem.isalpha()])

num = tuple([elem for elem in new_long_tup if elem.isdigit()])

lst = tuple([])
for a,n in zip(alph,num):
    print a,n

