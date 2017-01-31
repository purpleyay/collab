from flask import Flask
from flask import request
from flask import jsonify

from recommendations import get_all_pairings, get_most_common_pairing
import json

app = Flask(__name__)

with open('listens.json') as data_file:
     listens = json.load(data_file)
all_pairings = get_all_pairings(listens)

@app.route('/recommendations/', methods=['GET'])
def get_recommendations():
    subtopic = request.args.get('subtopic')
    pairings = get_most_common_pairing(all_pairings, subtopic)
    return jsonify(pairings)
