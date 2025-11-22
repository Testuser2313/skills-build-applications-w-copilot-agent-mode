
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
import datetime

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Leaderboard.objects.delete()
        Activity.objects.delete()
        Workout.objects.delete()
        User.objects.delete()
        Team.objects.delete()

        # Create teams
        marvel = Team(name='Marvel').save()
        dc = Team(name='DC').save()

        # Fetch teams
        marvel = Team.objects.get(name='Marvel')
        dc = Team.objects.get(name='DC')

        # Create users
        tony = User(name='Tony Stark', email='tony@marvel.com', team=marvel).save()
        steve = User(name='Steve Rogers', email='steve@marvel.com', team=marvel).save()
        bruce = User(name='Bruce Wayne', email='bruce@dc.com', team=dc).save()
        clark = User(name='Clark Kent', email='clark@dc.com', team=dc).save()

        # Fetch users
        tony = User.objects.get(email='tony@marvel.com')
        steve = User.objects.get(email='steve@marvel.com')
        bruce = User.objects.get(email='bruce@dc.com')
        clark = User.objects.get(email='clark@dc.com')

        # Create activities
        today = datetime.date.today()
        Activity(user=tony, type='Running', duration=30, date=today).save()
        Activity(user=steve, type='Cycling', duration=45, date=today).save()
        Activity(user=bruce, type='Swimming', duration=60, date=today).save()
        Activity(user=clark, type='Yoga', duration=20, date=today).save()

        # Create workouts
        w1 = Workout(name='Super Strength', description='Strength workout for heroes', suggested_for=[tony, steve, bruce, clark]).save()
        w2 = Workout(name='Flight Training', description='Aerobic workout for flyers', suggested_for=[clark, steve]).save()

        # Create leaderboard
        Leaderboard(team=marvel, points=100).save()
        Leaderboard(team=dc, points=90).save()

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
