from flask import Flask, abort, redirect, render_template, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "Alex", "surname": "Turner", "age": 36},
    {"id": 2, "name": "Thom", "surname": "Yorke", "age": 53},
]


@app.route("/")
def index():
    return redirect("/users")


@app.route("/users")
def users_page():
    return render_template("users.html", users=users)


@app.route("/create-user", methods=["get", "post"])
def create_user_page():
    message = ""

    if request.method == "GET":
        return render_template("create_user.html")

    name = request.form.get("name")
    surname = request.form.get("surname")
    age = request.form.get("age")

    if not name or not surname or not age:
        return render_template("create_user.html", message="ERROR: Empty fields (name, surname, age)")

    try:
        age = int(age)
    except:
        return render_template("create_user.html", message="ERROR: Invalid age")

    last_user_id = 0

    if len(users) > 0:
        last_user_id = users[-1]["id"]

    users.append({"id": last_user_id + 1, "name": name, "surname": surname, "age": age})
    return render_template("create_user.html", message="SUCCESS")


@app.route("/user/<int:user_id>")
def user_page(user_id):
    user = None

    for user_item in users:
        if user_item["id"] == user_id:
            user = user_item

    if user == None:
        return abort(404)

    return render_template("user.html", user=user)


if __name__ == "__main__":
    app.run(debug=True)
