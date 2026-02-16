from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Team Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='Team DC Superheroes')

        # Create Users
        users = [
            User(email='ironman@marvel.com', username='Iron Man', team=marvel),
            User(email='captain@marvel.com', username='Captain America', team=marvel),
            User(email='spiderman@marvel.com', username='Spider-Man', team=marvel),
            User(email='batman@dc.com', username='Batman', team=dc),
            User(email='superman@dc.com', username='Superman', team=dc),
            User(email='wonderwoman@dc.com', username='Wonder Woman', team=dc),
        ]
        for user in users:
            user.save()

        # Create Activities
        Activity.objects.create(user=users[0], activity_type='Running', duration=30, date='2024-01-01')
        Activity.objects.create(user=users[1], activity_type='Cycling', duration=45, date='2024-01-02')
        Activity.objects.create(user=users[3], activity_type='Swimming', duration=60, date='2024-01-03')
        Activity.objects.create(user=users[4], activity_type='Yoga', duration=40, date='2024-01-04')

        # Create Workouts
        w1 = Workout.objects.create(name='Pushups', description='Upper body strength')
        w2 = Workout.objects.create(name='Squats', description='Lower body strength')
        w1.suggested_for.set([users[0], users[3]])
        w2.suggested_for.set([users[1], users[4]])

        # Create Leaderboards
        Leaderboard.objects.create(team=marvel, total_points=150)
        Leaderboard.objects.create(team=dc, total_points=120)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
