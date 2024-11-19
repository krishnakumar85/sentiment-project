from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Use /sentiment to POST reviews'

@app.route('/sentiment')
def get_sentiment():
    if request.method == 'GET':
        return 'Use POST /sentiment to post reviews'
    if request.method == 'POST':
        request.get_json()
        # call method to send data to LLM




