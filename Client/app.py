from flask import request, Flask
from markupsafe import escape
import requests
import jwt

# this is the client, this should be the one that sends the request and JWT
app = Flask(__name__)

@app.route("/")
def hello():

    response = requests.post("http://localhost:5000/jwt", data={
        "token": jwt.encode({
            "user": "Gimble",
            "username": "gr1113",
            "priv": "tester"
        }, "password", algorithm="HS256")
    }).json()

    return f"<p>base64 encoded token: <strong>{response['token']}</strong> <br> decoded token: <strong>{response['decoded']}</strong></p>"