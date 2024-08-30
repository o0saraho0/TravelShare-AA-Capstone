from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    user1 = User(
        username="o0saraho0",
        first_name='Sarah',
        last_name='Jiang',
        email="sarah.jiang@example.com",
        password="password",
        profile_url="/images/profile_Sarah.JPG",
    )
    user2 = User(
        username="Rosebud",
        first_name='Rose',
        last_name='Montoya',
        email="rose.montoya@example.com",
        password="password",
        profile_url="/images/profile_Rose.jpeg",
    )
    user3 = User(
        username="Shanda",
        first_name='Shanda',
        last_name='Wang',
        email="shanda.wang@example.com",
        password="password",
        profile_url="/images/profile_Shanda.webp",
    )
    user4 = User(
        username="Hayden",
        first_name='Hayden',
        last_name='Galyean',
        email="hayden.galyean@example.com",
        password="password",
        profile_url="/images/profile_Hayden.jpeg",
    )
    user5 = User(
        username="Laiba",
        first_name='Laiba',
        last_name='Afzal',
        email="laiba.afzal@example.com",
        password="password",
        profile_url="/images/profile_Laiba.jpeg",
    )
    user6 = User(
        username="Mengxuan",
        first_name='Mengxuan',
        last_name='Liang',
        email="mengxuan.liang@example.com",
        password="password",
        profile_url="/images/profile_Mengxuan.png",
    )
    user7 = User(
        username="Caryn",
        first_name='Caryn',
        last_name='Wang',
        email="caryn.wang@example.com",
        password="password",
        profile_url="/images/profile_Caryn.webp",
    )
    user8 = User(
        username="Alan",
        first_name='Alan',
        last_name='Chang',
        email="alan.chang@example.com",
        password="password",
        profile_url="/images/profile_Alan.webp",
    )

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)
    db.session.add(user5)
    db.session.add(user6)
    db.session.add(user7)
    db.session.add(user8)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
