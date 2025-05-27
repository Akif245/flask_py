from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "He AI!"
@app.route('/bye')
def bye():
    return "Nikal..........."

@app.route('/<name>')
def greet(name):
    return f"Welcome {name}!"


if __name__=='__main__':
    app.run(debug=True)