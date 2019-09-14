imforms = ["i am", "i'm", "i a m", "i ' m", "i m", "im"]

async def checkIm(message):
    for form in imforms:
        nm = message.content.lower()
        if((form + " ") in nm):
            await message.channel.send("Hi " + nm[(nm.find(" " + form + " ") + len(form) + 2):] + " I'm walter!")

