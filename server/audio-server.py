from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
	return "it works"

@app.route('/save_audio', methods=['POST'])
def save_audio():
	with open('temp.mp3', 'wb') as f:
		f.write(request.data)
	return 'file saved'


app.run(host='0.0.0.0', port=7027, debug=True)
