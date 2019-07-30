gameStart = """
============================
DDu Du du~~~ (some silly sound)
Welcome to Ryan's H&C Game.
First, type the number of rounds
you want to play.
============================
"""

Answers = []


print(gameStart)
round = int(input("Round : "))
print("You are making " + str(round) + " round game.")
print ("Please type all the answers for each round.")

for x in range(round):
    Answers.append(
    int(input("Type the answer for Round " + str(x+ 1) + " : "))
    )





print(Answers)




while True:
    command = float((input("Guess the number")))
    if command > answer + 20 :
        print("Cold, Lower" )
    elif command > answer + 5 :
        print("Warm, Lower")
    elif command > answer :
        print("Hot, Lower")
    elif command == answer :
        print("you are right!")
        break
    elif command > answer - 5 :
        print("Hot, Higher")
    elif command > answer - 20 :
        print("Warm, Higher")
    else :
        print("Cold, Higher")



# while True:
#     command = int(input("Guess the number"))
#     if command > answer + 20 :
#         print("Cold,Lower" )
#     elif command > answer + 5 :
#         print("Warm, Lower")
#     elif command > answer :
#         print("Hot, Lower")
#     elif command < answer and command > answer - 5 :
#         print("Hot, Higher")
#     elif command < answer - 5 and command > answer - 10 :
#         print("Warm, Higher")
#     else :
#         print("Cold, Higher")
#     if command == answer :
#         print("You are Wrong.")

    # if command == answer :
    #     print("You are Wrong.")











    # number is 60
