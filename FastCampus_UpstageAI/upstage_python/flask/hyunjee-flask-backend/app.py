from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"


@app.route("/<username>")
def hell_user(username):
    return f"<h1>Hello, {username}!</h1>"


@app.route("/feed/<int:feed_id>")
def show_feed(feed_id):
    return f"<h1>FeedID : {feed_id}</h1>"


# API END POINT 생성


@app.route("/api/v1/feeds", methods=["GET"])
def get_all_feeds():
    data = {
        "status": "success",
        "feed": {
            "feed1": "data",
            "feed2": "data2",
        },
    }
    # python -> dict -> json
    return jsonify(data)


@app.route("/api/v1/feeds", methods=["POST"])
def create_feed():
    subject = request.form["subject"]
    content = request.form["content"]
    print(subject, content)

    return jsonify({"result": "success"})


if __name__ == "__main__":
    app.run()
