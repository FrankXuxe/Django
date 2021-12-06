from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.text


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:50]}..."


'''
Make an entry for Chess:
• The opening is the first part of the game, roughly the first ten moves or so. In the opening, it’s a good idea to do three things—bring out your bishops and knights, try to control the center of the board, and castle your king.
Make another entry for Chess:
• In the opening phase of the game, it’s important to bring out your bishops and knights. These pieces are powerful and maneuverable enough to play a significant role in the beginning moves of a game.
Make an entry for Rock Climbing:
• One of the most important concepts in climbing is to keep your weight on your feet as much as possible. There’s a myth that climbers can hang all day on their arms. In reality, good climbers have practiced specific ways of keeping their weight over their feet whenever possible.
'''
