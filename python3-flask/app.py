#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)
app.hits = 0

@app.route('/')
def hello():
	app.hits = app.hits + 1
	return 'Hello World! I have been seen %s times.' % app.hits

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8080, debug=True)

