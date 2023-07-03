from flask import Flask, render_template
import requests
# -------------------------------- CONSTANTS ------------------------------#
app = Flask(__name__)

@app.route("/")
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()

    return render_template("index.html", posts=all_posts)

@app.route("/post/<int:num>")
def get_post(num):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    post = all_posts[num-1]
    print(post)
    return render_template("post.html", post1=post)

@app.route("/contact")
def get_contact():
    return render_template("contact.html")

@app.route("/about")
def get_about():
    return render_template("about.html")






if __name__=="__main__":
    app.run(debug=True)