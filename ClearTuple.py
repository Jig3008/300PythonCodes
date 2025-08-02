try:
    a = (1,2,3,4)
    #Since we cannot clear a tuple we need a different mechanism for it
    temp_a = list(a)
    temp_a.clear()
    a = tuple(temp_a)
    print(a)
except:
    print('Program has an error!')