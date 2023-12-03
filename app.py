import os
from flask import Flask, jsonify
from flask_dotenv import DotEnv
from flask_mongoengine import MongoEngine
from models.player import Player

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

env = DotEnv()
env.init_app(app, os.path.join(basedir, ".env"))


app.config["MONGODB_SETTINGS"] = {
    "db": "GameService",
    "host": os.getenv("MONGO_URI"),
    "port": 27017
}

db = MongoEngine(app)

@app.route('/')
def home():
    return "Hello Flask";



@app.route('/player/<string:steam_id>')
def get_player(steam_id):
    print(steam_id)
    if steam_id == "steam_id":
        return jsonify({
            "Gamertag": "cuttingeyedjoe2"
        })
    else:
        player = Player(gamertag="cuttingeyedjoe", steam_id=steam_id)
        player.save()
        return jsonify(player)
   