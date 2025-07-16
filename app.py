from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Xin chào, đây là web Legend of Mushroom!"

if __name__ == "__main__":
    app.run()
