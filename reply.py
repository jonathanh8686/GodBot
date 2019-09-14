import random

imforms = ["i am", "i'm", "i a m", "i ' m", "i m", "im"]

async def checkIm(message):
    for form in imforms:
        nm = message.content.lower()
        if((form + " ") in nm):
            sendStr = "Hi " + message.content[(nm.find(" " + form + " ") + len(form) + 2):] + " I'm "
            if(random.random() <= 0.05):
                sendStr += "Walter!"
            else:
                sendStr += "walter!"
            await message.channel.send(sendStr)


async def checkWalter(message):
    nm = message.content.lower()
    if("walter" in nm):
        await message.channel.send("walter")
