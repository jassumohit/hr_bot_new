from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

app = Flask(__name__)

english_bot = ChatBot("HR Bot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
english_bot.set_trainer(ListTrainer)
#english_bot.set_trainer(ChatterBotCorpusTrainer)
#english_bot.train("chatterbot.corpus.english")
conv = open("C:/Users/mohit/Desktop/files.txt",'r').readlines()
english_bot.train(conv)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))


if __name__ == "__main__":
    app.run()
