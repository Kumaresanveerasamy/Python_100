from flask import Flask, render_template
import requests
from post import Post_page

app = Flask(__name__)
all_posts = requests.get("https://api.npoint.io/fb74cdc52273b54f6d40").json()
post_objects = []

for post in all_posts:
    posts_obj = Post_page(post["id"], post["body"], post["title"], post["subtitle"])
    post_objects.append(posts_obj)


@app.route("/")
def home():
    return render_template("index.html", content=post_objects)


@app.route("/post/<int:num>")
def required_post(num):
    requested_post = None
    for blogpost in post_objects:
        if blogpost.id == num:
            requested_post = blogpost
    return render_template("post.html", blog=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
