import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

os.system("git clone https://comrade09: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@github.com/comrade09/Telegram okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 -m Telegram main.py &")
