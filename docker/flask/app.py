from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Flask in Docker!"

app.run(host="0.0.0.0", port=5000)
