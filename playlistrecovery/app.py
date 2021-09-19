from flask import Flask, jsonify, session, render_template, redirect, url_for
from authlib.integrations.flask_client import OAuth
from loginpass import create_flask_blueprint, Google
from config import config
import time

app = Flask(__name__)

app.secret_key = config["app-secret"]
app.config["GOOGLE_CLIENT_ID"] = config["client-id"]
app.config["GOOGLE_CLIENT_SECRET"] = config["client-secret"]
app.config["GOOGLE_CLIENT_KWARGS"] = {
    "scope": "openid email profile https://www.googleapis.com/auth/youtube.readonly",
}
app.config["GOOGLE_AUTHORIZE_PARAMS"] = {
    "access_type": "offline",
}

oauth = OAuth()
oauth.init_app(app)

app_start_stamp = time.time()

@app.route('/')
def index():
    return render_template("index.html", app_start_stamp=app_start_stamp)
    #return '<ul><li><a href="/login/google">google</a></li></ul>'

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

def handle_authorize(remote, token, user_info):
    session["token"] = token
    session["user"] = user_info
    return redirect(url_for("index"))

@app.route("/test")
def test():
    params = {
        "part": "snippet,contentDetails",
        "mine": "true",
    }
    resp = oauth.google.get("youtube/v3/playlists", token=session["token"], params=params)
    resp.raise_for_status()
    return jsonify(resp.json())

bp = create_flask_blueprint([Google], oauth, handle_authorize)
app.register_blueprint(bp, url_prefix='')
