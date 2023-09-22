from django.db import models
from django.contrib.auth.models import User

# One topic can have many rooms, one room can have one topic - relationship


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    # since topic class id down you have to wrap it in 'quotes'
    # On deleting topic, room will be deleted, but will be set in database
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # null is set to be true so that the user is allowed to keep the description empty, blank is set to be true so that the user can submit the form as empty.
    participants = models.ManyToManyField(
        User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    # auto_now is set to be True so that when the room is updated, it updates the time also
    created = models.DateTimeField(auto_now_add=True)
    # auto_now_add is set to be True so that when the room is created, it stores the time and cannot be re-updated

    class Meta():
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name
    # this function returns the name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    # the above class Message forms a relationship with Room class(many to one), on deleting the room it deletes or cascades the data from the database
    body = models.TextField()
    # this forces the user to enter some value in the body
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta():
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]  # this trims down the message to 50chars
