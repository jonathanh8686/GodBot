import random

imforms = ["i am", "i'm", "i a m", "i ' m", "i m", "im"]

async def checkIm(message):
    for form in imforms:
        nm = message.content.lower()
        stind = -1

        if(nm.startswith(form)):
            stind = 0
        else:
            stind = nm.find(" " + form + " ") + 1

        if((form + " ") in nm):
            sendStr = "Hi " + message.content[(stind + len(form) + 1):] + " I'm "
            if(random.random() <= 0.05):
                sendStr += "Walter!"
            else:
                sendStr += "walter!"

            await message.channel.send(sendStr)
            break


async def checkWalter(message):
    nm = message.content.lower()
    if("walter" in nm):
        await message.channel.send("walter")
