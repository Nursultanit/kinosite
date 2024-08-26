from django.contrib import admin
from .models import UserProfile, Country, Director, Actor, Janre, Movie, Rating, Comment


admin.site.register(UserProfile)
admin.site.register(Country)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Janre)
admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(Comment)



