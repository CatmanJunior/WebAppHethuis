from flask import Flask
from flask import render_template, request, json, url_for, flash
import numpy as np
import cv2
import _thread


tTitle = "Projection App"
tContactH = "Problemen of vragen?"
tContactP = "Neem contact op met ons via: 0620949176"

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def main():

	error = None

	try:
		if request.method == "POST":
			_name1 = request.form['name1']
			_name2 = request.form['name2']
			_name3 = request.form['name3']
			_name4 = request.form['name4']
			_thread.start_new_thread( videoPlayer, (_name1, _name2, _name3, _name4))
			return render_template("index.html", title = tTitle, contactH = tContactH, contactP = tContactP, postText = "Changed to: " + _name1 + " " + _name2 + " "+ _name3+ " " + _name4)
	except Exception as error:
		pass

	return render_template("index.html", title = tTitle, contactH = tContactH, contactP = tContactP)



def videoPlayer(a,b,c,d):
	cap = cv2.VideoCapture('test.mp4')

	while(cap.isOpened()):
	    ret, frame = cap.read()
	    font = cv2.FONT_HERSHEY_SIMPLEX
	    cv2.putText(frame,a,(10,100), font, 4,(255,255,255),2,cv2.LINE_AA)
	    cv2.putText(frame,b,(200,500), font, 4,(255,255,255),2,cv2.LINE_AA)
	    cv2.putText(frame,c,(600,300), font, 4,(255,255,255),2,cv2.LINE_AA)
	    cv2.putText(frame,d,(100,600), font, 4,(255,255,255),2,cv2.LINE_AA)
	    cv2.imshow('frame',frame)
	    if cv2.waitKey(1) & 0xFF == ord('q'):
	        break

	cap.release()
	cv2.destroyAllWindows()

if __name__ == "__main__":
	app.debug = True
	app.run(host = '0.0.0.0',port=5005)