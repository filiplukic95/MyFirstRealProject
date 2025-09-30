from flask import Blueprint, render_template,request

auth = Blueprint("auth", __name__)

@auth.route("/login",methods=["GET", "POST"])
def login():
    data=request.form
    print(data)
    return render_template("login.html")

@auth.route("/logout")
def logout():
    pass

@auth.route("/sign-up",methods=["GET", "POST"])
def sign_up():
    if request.method=="POST":
        fullname=request.form.get("full-name")
        email=request.form.get("email")
        password=request.form.get("password")
        confirm_password=request.form.get("confirm-password")
    return render_template("register.html")


