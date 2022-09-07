import flask
import os
import json
import random
from datetime import datetime
from flask import send_from_directory

app = flask.Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/favicon.png')

@app.route('/')
@app.route('/home')
def home():
    now = datetime.now()
    new_time = now.strftime("%d/%m/%Y %H:%M:%S")
    ips = ['18.79.90.107', '13.81.30.116', '19.59.91.103', '21.19.110.127']
    selected_ip = random.choice(ips)
    
    responses = ['200', '401', '400', '404']
    selected_resp = random.choice(responses)
    
    dt = "{} - - [{} +0000] \"PUT /posts/posts/explore HTTP/1.0\" {} 4869 \"http://www.mcguire-martinez.info/faq.asp\" \"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/5320 (KHTML, like Gecko) Chrome/13.0.847.0 Safari/5320\"\n".format(selected_ip, new_time, selected_resp)
    return json.dumps(dt)

if __name__ == "__main__":
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run()
