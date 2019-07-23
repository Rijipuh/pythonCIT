tierList = [
{
"name" : "GrandMaster",
"min" : 4000
},
{
"name" : "Master",
"min" : 3500
},
{
"name" : "Diamond",
"min" : 3000
},
{
"name" : "Bronze",
"min" : 0
}
]

# while True :
InputSr = int(input("What is your sr? "))
if InputSr > tierList[0]["min"]:
    print (tierList[0]["name"])
elif InputSr > tierList[1]["min"]:
    print (tierList[1]["name"])
elif InputSr > tierList[2]["min"]:
    print (tierList[2]["name"])
else :
    print (tierList[3]["name"])

# standard = 3500
#
# Sr = int(input("What is your Sr? "))
#
# if Sr > standard:
#     print("You are a great Player!")
# elif Sr < standard:
#     print("You are absolute shit")
