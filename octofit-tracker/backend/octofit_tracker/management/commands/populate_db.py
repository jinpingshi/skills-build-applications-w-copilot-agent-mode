from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear all collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        # Create users (superheroes)
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='marvel'),
            User(email='captain@marvel.com', name='Captain America', team='marvel'),
            User(email='spiderman@marvel.com', name='Spider-Man', team='marvel'),
            User(email='batman@dc.com', name='Batman', team='dc'),
            User(email='superman@dc.com', name='Superman', team='dc'),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='dc'),
        ]
        User.objects.bulk_create(users)

        # Create activities
        activities = [
            Activity(user='Iron Man', type='run', duration=30),
            Activity(user='Captain America', type='cycle', duration=45),
            Activity(user='Spider-Man', type='swim', duration=25),
            Activity(user='Batman', type='run', duration=40),
            Activity(user='Superman', type='cycle', duration=60),
            Activity(user='Wonder Woman', type='swim', duration=35),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard
        Leaderboard.objects.create(team='marvel', points=100)
        Leaderboard.objects.create(team='dc', points=120)

        # Create workouts
        workouts = [
            Workout(name='Pushups', description='Do 20 pushups'),
            Workout(name='Running', description='Run for 30 minutes'),
            Workout(name='Cycling', description='Cycle for 45 minutes'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated octofit_db with test data'))
