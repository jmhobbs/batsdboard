import os
from flask import Flask
from batsdboard import BatsdBoard

app = Flask(__name__)

if os.getenv('BATSDBOARD_SETTINGS'):
    app.config.from_envvar('BATSDBOARD_SETTINGS')

BatsdBoard(app, '')
app.run()
