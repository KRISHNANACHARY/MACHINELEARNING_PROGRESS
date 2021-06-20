from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])

def index():
            return "<h1> This is Flask application </h1>"


if __name__ =="main__":
app.run()