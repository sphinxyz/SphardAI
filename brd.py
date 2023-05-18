from flask import Flask, render_template
from Bard import Chatbot

app = Flask(__name__, template_folder="./")

token = open('./token.txt', "r").read().strip('\n').strip()
bot = Chatbot(token)

@app.route('/')
def index():
    output = bot.ask("who are u?")['content']
    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)
