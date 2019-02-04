from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "El mejor bebe es bolita"

if __name__ == "__main__":
    application.run()
