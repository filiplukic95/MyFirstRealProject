from flask import Blueprint, render_template, jsonify,request,redirect,url_for,flash
from flask_login import login_required, current_user
from .models import Questions,Video, User
from . import db
import json
from werkzeug.security import check_password_hash,generate_password_hash
views = Blueprint("views", __name__)

@views.route('/')
def home():
    return render_template("index.html",user=current_user)

@views.route("/survey",methods=["GET","POST"])
@login_required
def survey():
    questions = Questions.query.all()
    result = []


    for q in questions:
        if q.stage==1:
            result.append({
            "type": "single",
            "question": q.question,
            "options": json.loads(q.options)
        })

    return render_template("survey.html",user=current_user,questions=result)

@views.route("/survey2",methods=["GET","POST"])
@login_required
def survey2():
    questions = Questions.query.all()
    result2=[]
    answer = request.form.get("pain-response")


    if answer == "yes":
        group="Extension"
    else:
        group="Flexion"
    for q in questions:
        if q.stage == 2 and q.v_group_name==group:
            result2.append({
                "type": "single",
                "question": q.question,
                "options": json.loads(q.options)
            })
    print(answer)
    return render_template("survey2.html",user=current_user,questions2=result2)

@views.route("/exercises")
@login_required
def exercises():
    group = 2
    videos=Video.query.filter_by(group_id=group)
    urls=[]
    titles=[]
    for v in videos:
            urls.append(v.url)
            titles.append(v.title)
    print(urls)
    print(titles)
    return render_template("exercises.html",user=current_user,title1=titles[0],title2=titles[1],url1=urls[0],url2=urls[1])

@views.route("/profile",methods=["GET","POST"])
@login_required
def profile():
    if request.method=="POST":
        act=request.form.get("act")
        if act=="change-info":
            full_name=request.form.get("full-name")
            phone=request.form.get("phone")
            date_of_birth=request.form.get("birthdate")
            city=request.form.get("city")
            state=request.form.get("state")

            user = User.query.filter_by(email=current_user.email).first()
            user.full_name=full_name
            user.phone=phone
            user.date_of_birth=date_of_birth
            user.city=city
            user.state=state
            db.session.commit()
            flash("Data has been saved!")
            return redirect(url_for("views.profile"))
        elif act=="change-pass":
            user=User.query.filter_by(email=current_user.email).first()
            password=request.form.get("current-password")
            if check_password_hash(user.password_hash,password):
                new_password=request.form.get("new-password")
                user.password_hash=generate_password_hash(new_password)
                db.session.commit()
                flash("Password changed successfully")
                return redirect(url_for("views.profile"))
            else:
                flash("That doesn't match the current password")
                return redirect(url_for("views.profile"))
    user=User.query.filter_by(email=current_user.email).first()
    return render_template("profile.html",user=current_user,email=current_user.email,
                           full_name=user.full_name,phone=user.phone,date_of_birth=user.date_of_birth,
                           city=user.city,state=user.state)