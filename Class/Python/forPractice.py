# target = int(input("type your target number : "))
# List = []
# for x in range( target + 1):
#     List.append(target * 6)
# print(List[target])


for x in range (100):
    if (x % 10) != 0 and (x % 10) % 3 == 0 :
        print("Clap!")
    else :
        print(x)
