Fibolist = [1, 1]
FiboOne = 1
FiboTwo = 1


# Fibolist.append(Fibolist[0] + Fibolist[1])
targetIndex = 300

# for x in range(2 , targetIndex + 1):
    # Fibolist.append(Fibolist[x-2] + Fibolist[x-1])
for i in range(targetIndex):
    temp = FiboTwo + FiboOne
    print(temp)
    FiboOne = FiboTwo
    FiboTwo = temp






# print(Fibolist[targetIndex])

# for loops
# print(range(30))
#
# for x in [0, 1, 2, 3, 4]:
#     print("normal List " + str(x))
#
# for x in range(5):
# #     print("range List " + str(x))
#
# for x in range(100):
#     if x % 2 == 1 :
#         print(x)
