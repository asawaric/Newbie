lst1 = [1, 2, 3, 4, 5, 6]
lst2 = []
lst3 = []

def sample_space_2(n):
    throws = [[i] for i in lst1] 
    for i in range(n-1):
        throws = [[i] + j for i in lst1 for j in throws]
    for elem in throws:
        lst2.append(sum(elem))

    return lst2
    
            


