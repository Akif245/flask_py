from flask import Flask,render_template
import random
import datetime

app = Flask(__name__)


@app.route('/')
def home():
      random_number = random.randint(0,9)
      return render_template ("1.html",nu=random_number,year=datetime.datetime.now().year,name="Akif")

if __name__=='__main__':
    app.run(debug=True  )