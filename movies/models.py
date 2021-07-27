from django.db import models
from django.utils import timezone

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movies(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    #actor_name = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Actor(models.Model):
    name = models.CharField(max_length=30)
    movie = models.ManyToManyField(Movies, through='Cast')

    def __str__(self):
        return self.name


class Cast(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['movie', 'actor']]
