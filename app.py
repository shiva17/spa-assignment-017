import flask
import os
from flask import send_from_directory

app = flask.Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/favicon.png')

@app.route('/')
@app.route('/home')
def home():
    return "18.79.90.107 - - [30/Aug/2022:07:01:25 +0000] \"PUT /posts/posts/explore HTTP/1.0\" 200 4869 \"http://www.mcguire-martinez.info/faq.asp\" \"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/5320 (KHTML, like Gecko) Chrome/13.0.847.0 Safari/5320\"\n"

if __name__ == "__main__":
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run()
