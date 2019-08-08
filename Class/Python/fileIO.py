file = open("../tier.txt", "a")
image = open("../Orisa.png", "rb")
bigImage = open("../../landscape.jpg", "rb")
createFile = open("./Diary/JHdiary0809.txt","w")

# print(file.read())
print(len(image.read()))
print(len(bigImage.read()))

Diary = input("write about your day : ")



createFile.write("Line Break test \n line breaked!")
