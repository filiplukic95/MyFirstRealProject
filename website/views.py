from flask import Blueprint, render_template, jsonify,request,redirect,url_for,flash,session
from flask_login import login_required, current_user
from .models import Questions,Video, User, Subscription
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
    if current_user.is_subscribed:

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
    else:
        return redirect(url_for("views.home"))

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
    session["group"]=group
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
    if current_user.is_subscribed:
        if session.get("group")=="Extension":
            group=1
        else:
            group=2
        videos=Video.query.filter_by(group_id=group)
        urls=[]
        titles=[]
        for v in videos:
                urls.append(v.url)
                titles.append(v.title)
        return render_template("exercises.html",user=current_user,title1=titles[0],title2=titles[1],url1=urls[0],url2=urls[1])
    else:
        flash("You are not subscribed! ", "popup")
        return redirect(url_for("views.home"))

@views.route("/profile",methods=["GET","POST"])
@login_required
def profile():
    url="views.profile"
    if request.method=="POST":

        act=request.form.get("act")

        if act=="change-info":

            user = User.query.filter_by(email=current_user.email).first()
            user.full_name=request.form.get("full-name")
            user.phone=request.form.get("phone")
            user.date_of_birth=request.form.get("birthdate")
            user.city=request.form.get("city")
            user.state=request.form.get("state")
            db.session.commit()

            flash("Data has been saved!","form-info")

            return redirect(url_for(url))
        elif act=="change-pass":
            user=User.query.filter_by(email=current_user.email).first()
            password=request.form.get("current-password")
            if check_password_hash(user.password_hash,password):
                new_password=request.form.get("new-password")
                user.password_hash=generate_password_hash(new_password)
                db.session.commit()
                flash("Password changed successfully","form-info")
                return redirect(url_for(url))
            else:
                flash("That doesn't match the current password","warning")
                return redirect(url_for(url))
    user=User.query.filter_by(email=current_user.email).first()

    last_sub=Subscription.query.filter_by(user_id=current_user.id).order_by(Subscription.end_date.desc()).first()
    return render_template("profile.html",user=current_user,sub=last_sub, email=current_user.email,
                           full_name=user.full_name,phone=user.phone,date_of_birth=user.date_of_birth,
                           city=user.city,state=user.state)

@views.route("/cancel-subscription", methods=["POST"])
@login_required
def cancel_sub():
    sub=Subscription.query.filter_by(user_id=current_user.id).first()
    if sub:
        sub.auto_renew=False
        db.session.commit()
        flash("Your subscription has been canceled. You will have access until "+sub.end_date.strftime('%d.%m.%Y.'),"popup")
    return redirect(url_for("views.profile"))