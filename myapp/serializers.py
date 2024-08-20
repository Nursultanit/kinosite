from rest_framework import serializers
from .models import UserProfile, Country, Director, Actor, Janre, Movie, Rating, Comment

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'  # Включает все поля модели в сериализаторе

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'  # Включает все поля модели в сериализаторе

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'  # Включает все поля модели в сериализаторе

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'  # Включает все поля модели в сериализаторе

class JanreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Janre
        fields = '__all__'  # Включает все поля модели в сериализаторе

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'  # Включает все поля модели в сериализаторе

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'  # Включает все поля модели в сериализаторе

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'  # Включает все поля модели в сериализаторе
