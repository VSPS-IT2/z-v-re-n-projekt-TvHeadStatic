from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title = "Blooger 1000")

@app.route("/post")
def post():
    return render_template("totalydone.html", title = "posting that 100% works")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("fourOfour.html", title = "FF ain't working suffer" ), 404

if __name__ == "__main__":
    app.run(debug=True)
