import os
from flask import Flask
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


@app.route("/")
def main_page():
    return "<p>Hello, World!</p>"


# run the app
if __name__ == "__main__":
    app.run(debug=True, port=8080, host='0.0.0.0')
