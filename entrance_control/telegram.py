import telepot


bot = telepot.Bot('636656567:AAGJNwvclwoJLHoice4DJkS_03H3m5Fpmso')
print("Trying to send")
bot.sendMessage('-1001403922890', 'FUCKING SHIT')
bot.sendPhoto('-1001403922890', open('./static/face.png', "rb"))
print("Sended")
