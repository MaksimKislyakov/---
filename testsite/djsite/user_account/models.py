from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    commission = models.CharField(max_length=100, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True)
    ACCESS_LEVELS = [
        (1, 'Viewer'),
        (2, 'Editor'),
        (3, 'Admin'),
    ]
    access_level = models.PositiveSmallIntegerField(choices=ACCESS_LEVELS, default=1)

    def __str__(self):
        return self.user.username

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()
    organizers = models.ManyToManyField(User, related_name='organized_events', blank=True)
    files = models.FileField(upload_to='event_files/', blank=True, null=True)
    tasks = models.TextField(blank=True, null=True)
    participants = models.ManyToManyField(User, related_name='events', blank=True)


    def __str__(self):
        return self.title
