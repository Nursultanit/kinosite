from django.shortcuts import render
from rest_framework import viewsets
from .models import (
    UserProfile,
    Country,
    Director,
    Actor,
    Janre,
    Movie,
    Rating,
    Comment
)
from .serializers import (
    UserProfileSerializer,
    CountrySerializer,
    DirectorSerializer,
    ActorSerializer,
    JanreSerializer,
    MovieSerializer,
    RatingSerializer,
    CommentSerializer
)

from django.shortcuts import render
from .models import Movie

def home_view(request):
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})

from django.shortcuts import render, get_object_or_404
from .models import Movie


def index(request):
    return render(request, 'index.html')

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})

def movie_detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    return render(request, 'movie_detail.html', {'movie': movie})




class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class JanreViewSet(viewsets.ModelViewSet):
    queryset = Janre.objects.all()
    serializer_class = JanreSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
