import os
import telegram

from flask import Flask, request
from telebot.credentials import WEBHOOK_URL
from telebot.mastermind import get_response

global bot
global TOKEN

TOKEN = os.getenv("TOKEN")

bot = telegram.Bot(token=BOT_TOKEN)

app = Flask(__name__)


@app.route('/{}'.format(BOT_TOKEN), methods=['POST'])
def respond():
    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    # get the chat_id to be able to respond to the same user
    chat_id = update.message.chat.id

    # get the message id to be able to reply to this specific message
    msg_id = update.message.message_id

    # Telegram understands UTF-8, so encode text for unicode compatibility
    text = update.message.text.encode('utf-8').decode()
    print("got text message :", text)

    # here we call our super AI
    response = get_response(text)
    # now just send the message back
    # notice how we specify the chat and the msg we reply to
    bot.sendMessage(chat_id=chat_id, text=response, reply_to_message_id=msg_id)
    return 'ok'


@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    # we use the bot object to link the bot to our app which live
    # in the link provided by URL
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=WEBHOOK_URL, HOOK=BOT_TOKEN))
    # something to let us know things work
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


@app.route('/')
def index():
    return '.'


if __name__ == '__main__':
    # note the threaded arg which allow
    # your app to have more than one thread
    app.run(threaded=True)
