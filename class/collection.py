# owChracter = ["tracer", "genji", 3, "Zarya", True ]
#
# print ( owChracter[1]  )
#

billBoard = [ "Old town road", "bad guy", "talk", "I dont care"]

# IwantToListen = 2


#
# print(" I want to listen rank {} of current billBoard".format(IwantToListen))
# print(billBoard[IwantToListen - 1])


Rank = input("which rank do you want to listen? ")

print("your rank {} music is {}".format(Rank, billBoard[int(Rank) - 1]))
