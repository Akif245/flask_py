from flask import Flask,render_template

app = Flask(__name__)
debug = True

@app.route('/')
def home():
      return '<h1 style="text-align:center">Hello World!</h1>' \
      '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmdqcjBjOTBlOTl2bGR6aXhlc2VkdW5yemhvZHp1dncxYWtsamF1ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Puc4FZWExJc0E/giphy.gif ">'
      
        #"""return render_template("akif.html")"""

'''@app.route("/<path:name>/<int:num>")
def greet(name,num):
      return f"Hello {name} ! you are {num} years old"
'''


@app.route('/bye')
def bye():
      return "bye"





if __name__=='__main__':
    app.run(debug=True  )