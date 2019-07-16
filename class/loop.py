# i = 0
# while True :
#     print("Obama is {} % American President!".format(i))
#     if i == 99 :
#         print( " i became 99. I quit.")
#         break
#     i += 1





# 1111 ~ 4444

# 1111
# 1112
# 1113
# 1114
# 1121
# 1122
# ...
# 4443
# 4444
num = ["1", "2", "3", "4"]
# numbs = ["1", "2", "3", "4"]
# numbers = ["1", "2", "3", "4"]
# number = ["1", "2", "3", "4"]

count = 0

for x in num:
    for y in num:
        for z in num:
            for a in num:
                print (x, y, z, a)

print ("I printed {} numbers".format(count))
