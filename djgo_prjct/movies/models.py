from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Person(models.Model):
    name = models.CharField(max_length=100)



class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    director = models.ForeignKey(Person, related_name='directory', on_delete=None)
    actors = models.ManyToManyField(Person, through='PersonMovie')
    year = models.IntegerField(validators=[MinValueValidator(1895), MaxValueValidator(2200)])



class PersonMovie(models.Model):
    role = models.CharField(max_length=100)
    person = models.ForeignKey(Person, on_delete=None)
    movie = models.ForeignKey(Movie, on_delete=None)
    





