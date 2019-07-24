Hamjji = {
"Ammo" : 10 ,
"Health" : 600 ,
"basicAdaptiveShield" : 100 ,
"additionalAdaptiveShieldPerEnemy" : 100,
"attackDamage" : 5

}

totalDamageDealt = 0

while True :
    command = input("press key : ")
    if command == "a" and Hamjji["Ammo"] > 0 :
        Hamjji["Ammo"] -= 1
        totalDamageDealt += Hamjji["attackDamage"]
        print("Hamjji has " + str(Hamjji["Ammo"]) + " Ammo Left")
        print("Hamjji dealt " + str(totalDamageDealt) + " Damages in total")
    elif command == "a" :
        Hamjji["Ammo"] = 10
        print ("Reloading..")
    elif command == "r":
        Hamjji["Ammo"] = 10
        print("relaoding...")
    elif command == "e":
        numberOfEnemiesAround = int(input("How many enemies are around Hamjji? "))
        Hamjji["Health"] += (Hamjji["basicAdaptiveShield"] + (Hamjji["additionalAdaptiveShieldPerEnemy"] * numberOfEnemiesAround))
        print("Hamjji's health is " + str(Hamjji["Health"]))
    elif command == "b":
        print ("Hamjji says hi!")
    elif command = "J" :
        print ("Hamjji is dancing :D")



numberOfEnemiesAround = int(input("How many enemies are around Hamjji? "))

print(
"Hamjji's health is " +
str((Hamjji["basicAdaptiveShield"] * numberOfEnemiesAround) + Hamjji["Health"]))
