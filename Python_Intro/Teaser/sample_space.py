import itertools
def outcomes(n):
    """ Returns a sample space of outcomes of n throws of a 6-sided die"""
    sample_space = []
    lst = range(1, 7)
    for i in itertools.product(lst, repeat=n):
        sample_space.append((i))
    return sample_space

  
