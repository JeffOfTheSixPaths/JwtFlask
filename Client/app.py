from flask import request, Flask,render_template
from markupsafe import escape
import requests
import jwt


# this is the client, this should be the one that sends the request and JWT
app = Flask(__name__)

@app.route("/")
def hello():

    d = {
        "token": jwt.encode({
            "user": "Gimble",
            "username": "gr1113",
            "priv": "tester"
        }, "password", algorithm="HS256")
    }

    response = requests.post("http://localhost:5000/simplejwt", data={
        "token": jwt.encode({
            "user": "Gimble",
            "username": "gr1113",
            "priv": "tester"
        }, "password", algorithm="HS256")
    })

    print(response.text)

    #output = f"<p>base64 encoded token: <strong>{response['token']}</strong> <br> decoded token: <strong>{response['decoded']}</strong></p>"
    #return output
    return render_template("index.html", JWT="testseter")

@app.route('/simplejwt', methods = ['POST'])
def send_simple():
    if request.method == 'POST':
        response = requests.post("http://localhost:5000/simplejwt", data={
            "token": jwt.encode({
                "user": "Gimble",
                "username": "gr1113",
                "priv": "tester"
            }, "password", algorithm="HS256")
        }).json()
        return response