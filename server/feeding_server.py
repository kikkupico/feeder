from flask import Flask
from Motor import feed
app = Flask(__name__)

@app.route('/feed_now', methods=['POST'])
def feed_now():
	feed()
	return 'Treat dispensed!'
	