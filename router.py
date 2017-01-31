from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/recommendations/')
def get_recommendations():
    subtopic = request.args.get('subtopic')
    # get function, return
    return 'Hello subtopic' + subtopic
