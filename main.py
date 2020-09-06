import flask
import random
from flask import render_template, request
import generateUwU
import generateOwO

app = flask.Flask(__name__)
app.config["DEBUG"] = False

@app.route('/', methods=['GET'])
def home():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def post():
	try:
		data = str(request.form['ip'])
		output_data = generateUwU.generateUwU(data)
		return render_template('index.html', output=output_data, output2='', input1=data)
	except:
		data = str(request.form['ipo'])
		output_data = generateOwO.text_to_owo(data)
		return render_template('index.html', output='', output2=output_data, input2 = data)
	

app.run( # Starts the site
	host='0.0.0.0',  # Establishes the host, required for repl to detect the site
	port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
)