f = open("censor.txt", "r")
swearWords = f.readlines()

def isSwear(word):
    if(word in swearWords):
        return True
    return False

for i in range(len(swearWords)):
    swearWords[i] = swearWords[i].strip()


test = input()
print(isSwear(test))
