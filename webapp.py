from flask import Flask
from flask import render_template, request, json

app = Flask(__name__)

@app.route("/")
def main():
	return render_template("index.html")

@app.route("/post", methods=['POST'])
def postData():
	_name1 = request.form['inputName1']
	_name2 = request.form['inputName2']
	_name3 = request.form['inputName3']
	_name4 = request.form['inputName4']

	if _name1 or _name2 or _name3 or _name4:
		return json.dumps({'html':'<span>GOOD!!</span>'})
	else:
		return json.dumps({'html':'<span>Enter one of the fields</span>'})

if __name__ == "__main__":
	app.run()

