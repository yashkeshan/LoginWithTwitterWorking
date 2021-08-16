import flask
from flask import Flask, request


app = Flask(__name__)

@app.route("/")
def root():
    app.do_teardown_appcontext()
    token = request.args.get("oauth_token")
    verifier = request.args.get("oauth_verifier")
    return flask.render_template('index.html')


def run_server():
    app.run(debug=True, port=5000)