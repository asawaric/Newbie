unflat = [[x,y] for x in range(6) for y in range(6) if y>x]
print unflat

new_sum_method = [sum((x*x) for x in range(1,201) if x%13==0 if x%2==0)]
print new_sum_method 
