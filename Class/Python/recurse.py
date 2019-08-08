facInput = int(input("type a number : "))

def getFac(num) :
    resultNum = 1
    for i in range(num):
        resultNum *= (i + 1)
    return resultNum

print(  getFac(facInput) )


def getFacRecurse(num) :
    if(num == 1) :
        return 1
    return num * getFacRecurse(num-1)

print(getFacRecurse(facInput))
