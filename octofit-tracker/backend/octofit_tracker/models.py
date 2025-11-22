# Models for users, teams, activities, leaderboard, and workouts using mongoengine
import mongoengine as me

class Team(me.Document):
    name = me.StringField(max_length=100, unique=True, required=True)
    meta = {'collection': 'teams'}

class User(me.Document):
    name = me.StringField(max_length=100, required=True)
    email = me.EmailField(unique=True, required=True)
    team = me.ReferenceField(Team, reverse_delete_rule=me.CASCADE, required=True)
    meta = {'collection': 'users'}

class Activity(me.Document):
    user = me.ReferenceField(User, reverse_delete_rule=me.CASCADE, required=True)
    type = me.StringField(max_length=100, required=True)
    duration = me.IntField(required=True)  # in minutes
    date = me.DateField(required=True)
    meta = {'collection': 'activities'}

class Workout(me.Document):
    name = me.StringField(max_length=100, required=True)
    description = me.StringField()
    suggested_for = me.ListField(me.ReferenceField(User))
    meta = {'collection': 'workouts'}

class Leaderboard(me.Document):
    team = me.ReferenceField(Team, reverse_delete_rule=me.CASCADE, required=True)
    points = me.IntField(required=True)
    meta = {'collection': 'leaderboard'}
