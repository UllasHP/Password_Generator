from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route("/", methods=["GET", "POST"])
def password_generator():
    if request.method == "POST":
        password_length = int(request.form["length"])
        password = generate_password(password_length)
        return render_template("index.html", generated_password=password)
    return render_template("index.html", generated_password="")

if __name__ == "__main__":
    app.run(debug=True)

