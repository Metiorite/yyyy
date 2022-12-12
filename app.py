import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

os.system("git clone https://Metiorite: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@github.com/Metiorite/FallenRobot okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 -m FallenRobot main.py &")
