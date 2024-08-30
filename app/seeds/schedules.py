from app.models import db, Schedule, environment, SCHEMA
from sqlalchemy.sql import text


def seed_schedules():
    schedule1 = Schedule(
        day="Day 1",
        itinerary_id=1
    )
    schedule2 = Schedule(
        day="Day 2",
        itinerary_id=1
    )
    schedule3 = Schedule(
        day="Day 3",
        itinerary_id=1
    )
    schedule4 = Schedule(
        day="Day 4",
        itinerary_id=1
    )
    schedule5 = Schedule(
        day="Day 5",
        itinerary_id=1
    )
    schedule6 = Schedule(
        day="Day 1",
        itinerary_id=2
    )
    schedule7 = Schedule(
        day="Day 2",
        itinerary_id=2
    )
    schedule8 = Schedule(
        day="Day 3",
        itinerary_id=2
    )
    schedule9 = Schedule(
        day="Day 1",
        itinerary_id=3
    )
    schedule10 = Schedule(
        day="Day 2",
        itinerary_id=3
    )
    schedule11 = Schedule(
        day="Day 3",
        itinerary_id=3
    )
    schedule12 = Schedule(
        day="Day 1",
        itinerary_id=4
    )
    schedule13 = Schedule(
        day="Day 2",
        itinerary_id=4
    )
    schedule14 = Schedule(
        day="Day 3",
        itinerary_id=4
    )
    schedule15 = Schedule(
        day="Day 4",
        itinerary_id=4
    )
    schedule16 = Schedule(
        day="Day 5",
        itinerary_id=4
    )
    schedule17 = Schedule(
        day="Day 6",
        itinerary_id=4
    )
    schedule18 = Schedule(
        day="Day 1",
        itinerary_id=5
    )
    schedule19 = Schedule(
        day="Day 2",
        itinerary_id=5
    )
    schedule20 = Schedule(
        day="Day 3",
        itinerary_id=5
    )
    schedule21 = Schedule(
        day="Day 4",
        itinerary_id=5
    )
    schedule22 = Schedule(
        day="Day 5",
        itinerary_id=5
    )
    schedule23 = Schedule(
        day="Day 6",
        itinerary_id=5
    )
    schedule24 = Schedule(
        day="Day 1",
        itinerary_id=6
    )
    schedule25 = Schedule(
        day="Day 2",
        itinerary_id=6
    )
    schedule26 = Schedule(
        day="Day 1",
        itinerary_id=7
    )
    schedule27 = Schedule(
        day="Day 2",
        itinerary_id=7
    )
    schedule28 = Schedule(
        day="Day 3",
        itinerary_id=7
    )
    schedule29 = Schedule(
        day="Day 4",
        itinerary_id=7
    )
    schedule30 = Schedule(
        day="Day 5",
        itinerary_id=7
    )
    schedule31 = Schedule(
        day="Day 1",
        itinerary_id=8
    )
    schedule32 = Schedule(
        day="Day 2",
        itinerary_id=8
    )
    schedule33 = Schedule(
        day="Day 3",
        itinerary_id=8
    )
    schedule34 = Schedule(
        day="Day 4",
        itinerary_id=8
    )
    schedule35 = Schedule(
        day="Day 5",
        itinerary_id=8
    )
    schedule36 = Schedule(
        day="Day 1",
        itinerary_id=9
    )
    schedule37 = Schedule(
        day="Day 2",
        itinerary_id=9
    )
    schedule38 = Schedule(
        day="Day 3",
        itinerary_id=9
    )
    schedule39 = Schedule(
        day="Day 4",
        itinerary_id=9
    )
    schedule40 = Schedule(
        day="Day 1",
        itinerary_id=10
    )
    schedule41 = Schedule(
        day="Day 2",
        itinerary_id=10
    )
    schedule42 = Schedule(
        day="Day 1",
        itinerary_id=11
    )
    schedule43 = Schedule(
        day="Day 2",
        itinerary_id=11
    )
    schedule44 = Schedule(
        day="Day 1",
        itinerary_id=12
    )
    schedule45 = Schedule(
        day="Day 2",
        itinerary_id=12
    )
    schedule46 = Schedule(
        day="Day 1",
        itinerary_id=13
    )
    schedule47 = Schedule(
        day="Day 2",
        itinerary_id=13
    )
    schedule48 = Schedule(
        day="Day 1",
        itinerary_id=14
    )
    schedule49 = Schedule(
        day="Day 2",
        itinerary_id=14
    )
    schedule50 = Schedule(
        day="Day 1",
        itinerary_id=15
    )
    schedule51 = Schedule(
        day="Day 2",
        itinerary_id=15
    )
    schedule52 = Schedule(
        day="Day 1",
        itinerary_id=16
    )
    schedule53 = Schedule(
        day="Day 2",
        itinerary_id=16
    )
    schedule54 = Schedule(
        day="Day 1",
        itinerary_id=17
    )
    schedule55 = Schedule(
        day="Day 2",
        itinerary_id=17
    )
    schedule56 = Schedule(
        day="Day 3",
        itinerary_id=17
    )
    schedule57 = Schedule(
        day="Day 1",
        itinerary_id=18
    )
    schedule58 = Schedule(
        day="Day 2",
        itinerary_id=18
    )
    schedule59 = Schedule(
        day="Day 1",
        itinerary_id=19
    )
    schedule60 = Schedule(
        day="Day 2",
        itinerary_id=19
    )
    schedule61 = Schedule(
        day="Day 1",
        itinerary_id=20
    )
    schedule62 = Schedule(
        day="Day 2",
        itinerary_id=20
    )

    db.session.add(schedule1)
    db.session.add(schedule2)
    db.session.add(schedule3)
    db.session.add(schedule4)
    db.session.add(schedule5)
    db.session.add(schedule6)
    db.session.add(schedule7)
    db.session.add(schedule8)
    db.session.add(schedule9)
    db.session.add(schedule10)
    db.session.add(schedule11)
    db.session.add(schedule12)
    db.session.add(schedule13)
    db.session.add(schedule14)
    db.session.add(schedule15)
    db.session.add(schedule16)
    db.session.add(schedule17)
    db.session.add(schedule18)
    db.session.add(schedule19)
    db.session.add(schedule20)
    db.session.add(schedule21)
    db.session.add(schedule22)
    db.session.add(schedule23)
    db.session.add(schedule24)
    db.session.add(schedule25)
    db.session.add(schedule26)
    db.session.add(schedule27)
    db.session.add(schedule28)
    db.session.add(schedule29)
    db.session.add(schedule30)
    db.session.add(schedule31)
    db.session.add(schedule32)
    db.session.add(schedule33)
    db.session.add(schedule34)
    db.session.add(schedule35)
    db.session.add(schedule36)
    db.session.add(schedule37)
    db.session.add(schedule38)
    db.session.add(schedule39)
    db.session.add(schedule40)
    db.session.add(schedule41)
    db.session.add(schedule42)
    db.session.add(schedule43)
    db.session.add(schedule44)
    db.session.add(schedule45)
    db.session.add(schedule46)
    db.session.add(schedule47)
    db.session.add(schedule48)
    db.session.add(schedule49)
    db.session.add(schedule50)
    db.session.add(schedule51)
    db.session.add(schedule52)
    db.session.add(schedule53)
    db.session.add(schedule54)
    db.session.add(schedule55)
    db.session.add(schedule56)
    db.session.add(schedule57)
    db.session.add(schedule58)
    db.session.add(schedule59)
    db.session.add(schedule60)
    db.session.add(schedule61)
    db.session.add(schedule62)
    db.session.commit()


def undo_schedules():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.schedules RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM schedules"))

    db.session.commit()
