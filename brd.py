from flask import Flask, render_template, request
from googletrans import Translator
from dotenv import load_dotenv
from Bard import Chatbot
import os

app = Flask(__name__, template_folder="./")

load_dotenv()  # Load environment variables from .env file

token = os.getenv("TOKEN")  # Get token from environment variable

bot = Chatbot(token)
translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])

@app.route('/', methods=['GET', 'POST'])
def index():
    output = ''
    if request.method == 'POST':
        command = request.form['command']
        translated_command = translator.translate(command, src='id', dest='en').text
        translated_output = bot.ask(translated_command)['content']
        output = translator.translate(translated_output, src='en', dest='id').text
    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)
