def RGTestFunction(n):
    tmpString = [x for x in str(n)]
    for i in range(1,len(tmpString),1):
        if i%3==0 and i != 0:
            tmpString[-i]="."+tmpString[-i]
    return "".join(tmpString)
        
print(RGTestFunction(10000000000000000000))
