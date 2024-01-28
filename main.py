import telebot
import requests

token = ''

bot = telebot.TeleBot(token)

def reqapi(ip):
    url = f'https://ipinfo.ip/{ip}/geo'
    r = requests.get(url).json()
    return r
    
@bot.message_handler(commands=['start'])
def start(massage):
    msg = bot.send_message(massage.chat.id, f'hello: {massage.from_user.username}/n Введи IP:')
    bot.register_next_step_handler(msg, getip)

def getip(massage):
    ip = massage.text
    res = str(reqapi(ip))
    bot.send_message(massage.chat_id, res)


if __name__=='__main__':
    bot.infinity_polling()