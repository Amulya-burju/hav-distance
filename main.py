from flask import Flask, render_template, url_for, request
from forms import distanceform
import sys
from haversine import haversine 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c87c58ad376b0ca5b4e3085ea82400bf'
@app.route("/")
@app.route("/home")
def home():
   return render_template('home.html')

@app.route("/about")
def about():
   return render_template('about.html', title= 'About')


if __name__ == '__main__':
    app.run(debug=True)