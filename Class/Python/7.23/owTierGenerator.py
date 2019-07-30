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
"name" : "Platinum",
"min" : 2500
},
{
"name" : "Gold",
"min" : 2000
},
{
"name" : "Silver",
"min" : 1500
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
elif InputSr > tierList[3]["min"]:
    print (tierList[3]["name"])
elif InputSr > tierList[4]["min"]:
    print (tierList[4]["name"])
elif InputSr > tierList[5]["min"]:
    print (tierList[5]["name"])
else :
    print (tierList[6]["name"])

# standard = 3500
#
# Sr = int(input("What is your Sr? "))
#
# if Sr > standard:
#     print("You are a great Player!")
# elif Sr < standard:
#     print("You are absolute shit")
