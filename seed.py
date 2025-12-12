from website import db, create_app
from website.models import Questions
import json
app = create_app()

with app.app_context():
    q1 = Questions(
        question="Gde si brate moj?",
        stage=2,
        v_group_name="Flexion",
        options=json.dumps([
        "Svuda", "Tu i tamo", "Po malo", "Ne"
        ])
    )

    q2 = Questions(
        question="Levo desno tamo vamo?",
        stage=2,
        v_group_name="Flexion",
        options=json.dumps([
            "It hurts", "Why so much?", "Here and there", "Too much"
        ])
    )

    db.session.add_all([q1, q2])
    db.session.commit()
    print("Test questions inserted successfully.")
