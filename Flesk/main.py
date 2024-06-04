from flask import *

app = Flask(__name__)

array_of_posts = [
    ["Title", "Username", "Content"]
]

@app.route("/")
def index():
    print(str(array_of_posts))
    return render_template("index.html", title = "Blooger 1000", current_posts = array_of_posts)

@app.route("/post", methods=["GET", "POST"])
def post():
    global array_of_posts
    match(request.method):
        case "POST":
            print(str(request.form))
            array_of_posts = [[request.form["title"], request.form["author"], request.form["content"]]] + array_of_posts
            return redirect("/", code=302)
        case _:
            return render_template("totalydone.html", title = "posting that 100% works")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("fourOfour.html", title = "FF ain't working suffer" ), 404

if __name__ == "__main__":
    app.run(debug=True)
