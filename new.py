from flask import Flask,render_template
from serial import Serial

app = Flask(__name__)
#ser=Serial(/dev/ttyUSB0,9600)

@app.route('/')
def home():
	return render_template("home.html")

@app.route("/navigate/<direction>")
def navigation(direction):
	if (direction == "forward"):
		ser.write(b'150,0,150,0')
	elif(direction == "reverse"):
		ser.write(b'0,150,0,150')
	elif (direction == "left"):
		ser.write(b'0,150,150,0')
	elif (direction == "right"):
		ser.write(b'150,0,0,150')
	elif (direction == "stop"):
		ser.write(b'0,0,0,0')
	return ''

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000,debug="True")