from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
        return render_template("akif.html")
    # return '<h1 style="text-align:center">Hello World!</h1>' \
    #        '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmdqcjBjOTBlOTl2bGR6aXhlc2VkdW5yemhvZHp1dncxYWtsamF1ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Puc4FZWExJc0E/giphy.gif ">'

if __name__=='__main__':
    app.run(debug=True  )