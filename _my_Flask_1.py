from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_1.db'
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)
    user_phone = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Post %r>' % self.title

@app.route('/')
def index():
    return render_template("index.html")


# def create_user(username, password, user_phone, email):
#     user = Users(username=username, password=password, user_phone=user_phone, email=email)
#     db.session.add(user)
#     db.session.commit()

@app.route("/posts")
def posts():
    posts = Post.query.all()
    return render_template("posts.html", posts=posts)


@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        text = request.form["text"]

        post = Post(title=title, text=text)

        try:
            db.session.add(post)
            db.session.commit()
            return render_template("index.html")
        except:
            return "Помилка"

    return render_template("create.html")



@app.route("/about")
def about():
    return render_template("about.html")



if __name__ == "__main__":
    app.run(debug=True)