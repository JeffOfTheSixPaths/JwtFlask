from flask import request, Flask
from markupsafe import escape
import jwt

app = Flask(__name__)

@app.route("/")
def hello():
    name = request.args.get("name", "Flask")
    return f"Hello, {escape(name)}!"

@app.route("/jwt", methods = ['POST', 'GET']) # GET needs to be removed in production, this is just for testing
def handle_tokens():
    if request.method == 'POST':
        print("received thing")
        if request.form["token"]:
            token = request.form["token"]

            return {
                "token": token,
                "decoded": jwt.decode(token, "password", algorithms=["HS256"])
            }
            #return f" {token}--------------------------{jwt.decode(token, 'password', algorithms=['HS256'])}"
