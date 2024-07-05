from flask import Flask, render_template, request
import telebot

# Замени на свой API-ключ
API_KEY = '7121996431:AAG9_-LyjNxwPTbLjx9eR9vRClAe1XeHd28'

app = Flask(__name__)
bot = telebot.TeleBot(API_KEY)

click_count = 0

@app.route('/')
def index():
    return render_template('clckcode.html', click_count=click_count)

@app.route('/click', methods=['POST'])
def click():
    global click_count
    click_count += 1
    bot.send_message(chat_id='5394056862', text=f"Кликнули {click_count} раз(а)!")
    return str(click_count)

if __name__ == '__main__':
    app.run()
