def gen_dict():
    mydict = {}
    for element in range(1, 16):
        mydict[element] = element ** 2
    return mydict
    
result = gen_dict()
print(result)


