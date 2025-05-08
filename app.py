from flask import Flask
app = flask(__name__)

@app.route('/')
def hello():
    return "I love you kututpatutu"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')