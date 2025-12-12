from flask import Blueprint, render_template, jsonify,request
from flask_login import login_required, current_user
from .models import Questions
import json
views = Blueprint("views", __name__)

@views.route('/')
def home():
    return render_template("index.html",user=current_user)

@views.route("/survey",methods=["GET","POST"])
@login_required
def survey():
    questions = Questions.query.all()
    result = []
    result2=[]
    answer = request.form.get("pain-form")


    if answer == "yes":
        group="Extension"
    else:
        group="Flexion"
    for q in questions:
        if q.stage==1:
            result.append({
            "type": "single",
            "question": q.question,
            "options": json.loads(q.options)
        })
        elif q.stage == 2 and q.v_group_name==group:
            result2.append({
                "type": "single",
                "question": q.question,
                "options": json.loads(q.options)
            })

    return render_template("survey.html",user=current_user,questions=result,questions2=result2)

@views.route("/survey2",methods=["GET","POST"])
@login_required
def survey2():
    questions = Questions.query.all()
    result = []
    result2=[]
    answer = request.form.get("pain-response")


    if answer == "yes":
        group="Extension"
    else:
        group="Flexion"
    for q in questions:
        if q.stage==1:
            result.append({
            "type": "single",
            "question": q.question,
            "options": json.loads(q.options)
        })
        elif q.stage == 2 and q.v_group_name==group:
            result2.append({
                "type": "single",
                "question": q.question,
                "options": json.loads(q.options)
            })
    print(answer)
    return render_template("survey2.html",user=current_user,questions2=result2)