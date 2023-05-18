from flask import Flask, render_template, request
from googletrans import Translator
from Bard import Chatbot

app = Flask(__name__, template_folder="./")

token = open('./token.txt', "r").read().strip('\n').strip()
bot = Chatbot(token)
translator = Translator()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        command = request.form['command']
        translated_command = translator.translate(command, src='id', dest='en').text
        translated_output = bot.ask(translated_command)['content']
        output = translator.translate(translated_output, src='en', dest='id').text
    else:
        output = ''

    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)
