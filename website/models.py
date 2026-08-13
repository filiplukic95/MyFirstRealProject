

from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime, timezone


class Questions(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    question=db.Column(db.String(1000),nullable=False)
    options=db.Column(db.String(1000),nullable=False)
    stage=db.Column(db.Integer,nullable=False)
    v_group_name=db.Column(db.String(120),db.ForeignKey("video_group.name"))
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    full_name = db.Column(db.String(120), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    phone=db.Column(db.Integer)
    date_of_birth=db.Column(db.Text)
    state=db.Column(db.String(120))
    city=db.Column(db.String(120))
    subscriptions=db.relationship("Subscription", backref="owner",lazy=True)
    @property
    def is_subscribed(self):
        last_sub=Subscription.query.filter_by(user_id=self.id).order_by(Subscription.end_date.desc()).first()
        if last_sub and last_sub.end_date>datetime.now(timezone.utc).replace(tzinfo=None):
            return True
        return False

class Subscription(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    begin_date=db.Column(db.DateTime, nullable=False,default=datetime.now(timezone.utc))
    end_date=db.Column(db.DateTime,nullable=False)
    status=db.Column(db.String(20),default="Active")
    user_id=db.Column(db.Integer,db.ForeignKey("user.id"),nullable=False)
    auto_renew=db.Column(db.Boolean,default=True)
    stripe_subscription_id=db.Column(db.String(100))

class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    stage = db.Column(db.Integer,db.ForeignKey("questions.stage"))
    answers = db.Column(db.Text)   # JSON format
    completed_at = db.Column(db.DateTime(timezone=True), default=func.now())

class VideoGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    url = db.Column(db.String(200))
    group_id = db.Column(db.Integer, db.ForeignKey('video_group.id'))
    format=db.Column(db.String(200))
    DurationInSeconds=db.Column(db.Integer)
    size=db.Column(db.Integer)
    DateAdded=db.Column(db.DateTime(timezone=True), default=func.now())

class UserVideoAccess(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    video_id = db.Column(db.Integer, db.ForeignKey('video.id'))
    granted_at = db.Column(db.DateTime(timezone=True), default=func.now())


