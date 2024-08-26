from flask.cli import AppGroup
from .activities import seed_activities, undo_activities
from .categories import seed_categories, undo_categories
from .collections import seed_collections, undo_collections
from .itineraries import seed_itineraries, undo_itineraries
from .schedules import seed_schedules, undo_schedules
from .reviews import seed_reviews, undo_reviews
from .users import seed_users, undo_users


from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo 
        # command, which will  truncate all tables prefixed with 
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_reviews()
        undo_collections()
        undo_activities()
        undo_schedules()
        undo_itineraries()
        undo_categories()
        undo_users()
    seed_users()
    seed_categories()
    seed_itineraries()
    seed_schedules()
    seed_activities()
    seed_collections()
    seed_reviews()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_reviews()
    undo_collections()
    undo_activities()
    undo_schedules()
    undo_itineraries()
    undo_categories()
    undo_users()
    # Add other undo functions here
