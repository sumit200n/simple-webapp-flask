import os
from flask import Flask
app = Flask(__name__)

hname = os.uname()
print(hname)

@app.route("/")
def main():
    return (str(hname))

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
