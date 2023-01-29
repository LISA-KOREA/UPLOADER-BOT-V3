from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'UPLOADER-BOT-V3'


if __name__ == "__main__":
    app.run()
