from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
	name = request.form['name']
	location = request.form['location'].title()
	language = request.form['language']
	comments = request.form['comments']
	return render_template('result.html', name=name, location=location, language=language, comments=comments)

app.run(debug = True)
