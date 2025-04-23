from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for OctoFit Tracker'

    def handle(self, *args, **kwargs):
        # Drop existing collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Users
        user1 = User.objects.create(username="thundergod", email="thundergod@mhigh.edu", password="thundergodpassword")
        user2 = User.objects.create(username="metalgeek", email="metalgeek@mhigh.edu", password="metalgeekpassword")
        user3 = User.objects.create(username="zerocool", email="zerocool@mhigh.edu", password="zerocoolpassword")
        user4 = User.objects.create(username="crashoverride", email="crashoverride@mhigh.edu", password="crashoverridepassword")
        user5 = User.objects.create(username="sleeptoken", email="sleeptoken@mhigh.edu", password="sleeptokenpassword")

        # Create Teams
        team1 = Team.objects.create(name="Blue Team")
        team2 = Team.objects.create(name="Gold Team")
        team1.members.add(user1, user2)
        team2.members.add(user3, user4, user5)

        # Create Activities
        Activity.objects.create(user=user1, activity_type="Cycling", duration=timedelta(hours=1))
        Activity.objects.create(user=user2, activity_type="Crossfit", duration=timedelta(hours=2))
        Activity.objects.create(user=user3, activity_type="Running", duration=timedelta(hours=1, minutes=30))
        Activity.objects.create(user=user4, activity_type="Strength", duration=timedelta(minutes=30))
        Activity.objects.create(user=user5, activity_type="Swimming", duration=timedelta(hours=1, minutes=15))

        # Create Leaderboard Entries
        Leaderboard.objects.create(user=user1, score=100)
        Leaderboard.objects.create(user=user2, score=90)
        Leaderboard.objects.create(user=user3, score=95)
        Leaderboard.objects.create(user=user4, score=85)
        Leaderboard.objects.create(user=user5, score=80)

        # Create Workouts
        Workout.objects.create(name="Cycling Training", description="Training for a road cycling event")
        Workout.objects.create(name="Crossfit", description="Training for a crossfit competition")
        Workout.objects.create(name="Running Training", description="Training for a marathon")
        Workout.objects.create(name="Strength Training", description="Training for strength")
        Workout.objects.create(name="Swimming Training", description="Training for a swimming competition")

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data for OctoFit Tracker.'))
