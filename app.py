from flask import Flask
app = Flask(name)

@app.route('/')
def hello_world():
    return 'Made with Love by @activ3'


if name == "main":
    app.run()
