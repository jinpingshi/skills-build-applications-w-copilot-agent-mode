from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # 清空所有集合
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # 创建队伍
        Team.objects.create(name='marvel')
        Team.objects.create(name='dc')

        # 创建用户（超级英雄）
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='marvel'),
            User(email='captain@marvel.com', name='Captain America', team='marvel'),
            User(email='spiderman@marvel.com', name='Spider-Man', team='marvel'),
            User(email='batman@dc.com', name='Batman', team='dc'),
            User(email='superman@dc.com', name='Superman', team='dc'),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='dc'),
        ]
        User.objects.bulk_create(users)

        # 创建活动
        activities = [
            Activity(user='Iron Man', type='run', duration=30),
            Activity(user='Captain America', type='cycle', duration=45),
            Activity(user='Spider-Man', type='swim', duration=25),
            Activity(user='Batman', type='run', duration=40),
            Activity(user='Superman', type='cycle', duration=60),
            Activity(user='Wonder Woman', type='swim', duration=35),
        ]
        Activity.objects.bulk_create(activities)

        # 创建排行榜
        Leaderboard.objects.create(team='marvel', points=100)
        Leaderboard.objects.create(team='dc', points=120)

        # 创建锻炼
        workouts = [
            Workout(name='Pushups', description='Do 20 pushups'),
            Workout(name='Running', description='Run for 30 minutes'),
            Workout(name='Cycling', description='Cycle for 45 minutes'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db 已成功填充测试数据'))
