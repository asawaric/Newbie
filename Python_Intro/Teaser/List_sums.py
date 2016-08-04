lst = [1,2,3,4,5,6]
def sample_space(n):
    throws = [[i] for i in lst]
    for k in range(n-1):
        throws = [i + [j] for i in throws for j in lst]
    lst2 = [sum(i) for i in throws]
    return lst2
    

