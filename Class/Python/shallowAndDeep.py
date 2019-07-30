president = ["Obama", "Trump", "Bush", "Clinton"]

presidentShallowCopy = president
presidentDeepCopy = president.copy()

# print(presidentShallowCopy)


presidentShallowCopy[2] = "Will Smith"
presidentDeepCopy[3] = "Johnny Depp"
print(president)
print(presidentShallowCopy)
print(presidentDeepCopy)
