def detect369(num) :
    strumber = str(num)
    returnSting = ""
    for x in strumber:
        if (x == '3' or x == "6" or x == "9") :
            returnSting += "clap!"

    if(returnSting == "") :
        return num
    else :
        return returnSting

    # return(num**2)

def get369Cnt(num, divider = 10, count = 0) :
    if (num == 0) :
        return count
    x = (num % divider) / (divider / 10)
    if (x == 3 or x == 6 or x == 9) :
        return get369Cnt(num - x * (divider / 10) , divider * 10, count + 1)
    else :
        return get369Cnt(num - x * (divider /10) , divider * 10, count)



def detect369Rec(num):
    cnt = get369Cnt(num)
    returnSting = ""
    for x in range(cnt):
            returnSting += "clap!"

    if(returnSting == "") :
            return num
    else :
            return returnSting





for x in range (900):
    print(detect369Rec(x))



    # if (x % 10) != 0 and (x % 10) % 3 == 0 :
    #     print("Clap!")
    # elif x > 29 and x < 40 :
    #     print("Clap!")
    # else :
    #     print(x)
