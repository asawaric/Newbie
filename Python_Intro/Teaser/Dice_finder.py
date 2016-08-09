from Black_box_new import Black_box
def dice_finder(n, m=1000):
    dict3 = {}
    for i in range((n/6), (n+1)):
        dict2 = Black_box(i, m)
        for x in dict2.keys():
            if x == 51:       
               dict3[i] = dict2[x]
    print dict3        

dice_finder(100, 1000)
        

        


