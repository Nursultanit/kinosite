from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

class UserProfile(models.Model):
    nickname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(blank=True, null=True)
    STATUS_CHOICES = [('Pro', 'Pro'), ('Simple', 'Simple')]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

class Country(models.Model):
    country_name = models.CharField(max_length=255)

class Director(models.Model):
    director_name = models.CharField(max_length=255)
    bio = models.TextField()
    age = models.IntegerField()
    director_image = models.ImageField(upload_to='directors/')

class Actor(models.Model):
    actor_name = models.CharField(max_length=255)
    bio = models.TextField()
    age = models.IntegerField()
    actor_image = models.ImageField(upload_to='actors/')

class Janre(models.Model):
    janre_name = models.CharField(max_length=255)

class Movie(models.Model):
    MOVIE_TYPE_CHOICES = [
        ('144', '144'),
        ('360', '360'),
        ('480', '480'),
        ('720', '720'),
        ('1080', '1080'),
        ('1080 Ultra', '1080 Ultra'),
    ]
    movie_name = models.CharField(max_length=255)
    release_date = models.DateField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actor)
    janres = models.ManyToManyField(Janre)
    type = models.CharField(max_length=20, choices=MOVIE_TYPE_CHOICES)
    movie_time = models.DurationField()
    description = models.TextField()
    movie_trailer = models.URLField()
    movie_image = models.ImageField(upload_to='movies/')
    movie = models.FileField(upload_to='movies/')
    STATUS_CHOICES = [('Pro', 'Pro'), ('Simple', 'Simple')]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

class Rating(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, i) for i in range(1, 11)])

class Comment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='replies')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


