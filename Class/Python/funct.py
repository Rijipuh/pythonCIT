# def my_function(food):
#   for x in food:
#     print(x)
#   return ("Nothing")
#
# fruits = ["apple", "banana", "cherry"]
#
# print(my_function(fruits))

# print(print("asdf"))

# question  = [[78, 692, -7650], [-37, 92, 1311], [-67, -523, 61]]
#
# def quadraticFormula(a,b,c) :
#     plusRoot = (-b + (b * b - 4 * a * c) ** (1/2) ) / ( 2 * a )
#     minusRoot = (-b - (b * b - 4 * a * c) ** (1/2) ) / ( 2 * a )
#
#     return [plusRoot ,minusRoot]
#
#
#
#
# # print(quadraticFormula(78,692,-7650))
# # print(quadraticFormula(-37,92,1311))
# # print(quadraticFormula(-67,-523,61))
#
# for quiz in question :
#     print( quadraticFormula(quiz[0], quiz[1], quiz[2]) )
#
#
# # print(quadraticFormula(1,-4,-12))




#
# def mimicRange(rangeNum) :
#     resultlist = []
#     count = 0
#     while count < rangeNum :
#         resultlist.append(count)
#         count += 1
#     return (resultlist)
#
# print(mimicRange(324))
#
# for x in mimicRange(300):
#     print("I am" + str(x))


def mimicAppend(Data,List) :
    NewList = List + [ Data ]
    return NewList


a = [" R", "J"]
print(mimicAppend("P", a))
# a.append("K")





# mimicRange(300)
