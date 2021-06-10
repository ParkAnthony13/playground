from flask import Flask, render_template

app = Flask(__name__)    

@app.route('/')
def home():
    return "Home Page"

@app.route('/play/<int:times>/<color>')
def index(times,color):
    return render_template('index.html',mult=times,color=color)

if __name__=="__main__":
    app.run(debug=True)