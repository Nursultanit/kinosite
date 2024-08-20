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


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'birth_date', 'country']
    search_fields = ['user__username']

class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class DirectorAdmin(admin.ModelAdmin):
    list_display = ['name', 'birth_date']
    search_fields = ['name']

class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'birth_date']
    search_fields = ['name']

class JanreAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'release_date', 'director']
    search_fields = ['title', 'director__name']

class RatingAdmin(admin.ModelAdmin):
    list_display = ['movie', 'user', 'rating']
    search_fields = ['movie__title', 'user__username']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['movie', 'user', 'content', 'created_at']
    search_fields = ['movie__title', 'user__username']