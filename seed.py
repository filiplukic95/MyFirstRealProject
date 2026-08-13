from website import db, create_app
from website.models import User,Subscription
import json
from datetime import datetime, timedelta, timezone

app = create_app()

with app.app_context():
    me=User.query.filter_by(email="mirko@gmail.com").first()

    sub=Subscription(end_date=datetime.now(timezone.utc)+timedelta(days=30),owner=me)

    db.session.add(sub)
    db.session.commit()
    print("Test questions inserted successfully.")
