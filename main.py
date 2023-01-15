from flask import Flask, render_template, request
from post_class import GetPost
from email_class import SendEmail

app = Flask(__name__)
my_tool = GetPost()


@app.route("/")
def home_page():
    my_blog = my_tool.get_data()
    return render_template("index.html", blog_list=my_blog)


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/post/<int:number>")
def post_page(number):
    my_blog = my_tool.get_data()[number - 1]
    return render_template("post.html", blog_post=my_blog)


@app.route("/contact", methods=["POST", "GET"])
def contact_page():
    if request.method == "GET":
        return render_template("contact.html", my_answer="Contact Me")
    elif request.method == "POST":
        user_name = request.form["userName"]
        user_email = request.form["userEmail"]
        user_phone = request.form["userPhone"]
        user_message = f'By {user_name} \n{request.form["userMessage"]} \nmy phone number: {user_phone}'
        my_gmail = SendEmail(sender=user_email, subject="Message Via Your Blog", body=user_message)
        my_gmail.send_mail()
        return render_template("contact.html", my_answer="Your Message sent successfully")


if __name__ == "__main__":
    app.run(debug=True)
