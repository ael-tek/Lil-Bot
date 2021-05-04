# pylint: disable=missing-module-docstring
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from flask import Flask, render_template, request

bot = ChatBot('Skeleton',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3',
    gic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter']
)
trainer = ListTrainer(bot)
conversation = ["ping"]
trainer.train(conversation)
        
app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")

def get_box_response():
    userText = request.args.get('msg')
    if userText=='ping':
        return str('pong')
    if userText=='pong':
        return str('ping')
#return str(bot.get_response(userText))
#user=input("Enter your name: ")
#print ("Welcome!")
#while True:
 #   request=input(user+':')
  #  if request=='ping':
   #     print(bot.name+': pong')
    #    break
   # if request=='pong':
    #    print(bot.name+': ping')
    #   break
if __name__ == "__main__":
   app.run(debug=True)
   