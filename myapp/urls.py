from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='user_list'),
    path('users/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user_detail'),

    path('countries/', CountryViewSet.as_view({'get': 'list', 'post': 'create'}), name='country_list'),
    path('countries/<int:pk>/', CountryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='country_detail'),

    path('directors/', DirectorViewSet.as_view({'get': 'list', 'post': 'create'}), name='director_list'),
    path('directors/<int:pk>/', DirectorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='director_detail'),

    path('actors/', ActorViewSet.as_view({'get': 'list', 'post': 'create'}), name='actor_list'),
    path('actors/<int:pk>/', ActorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='actor_detail'),

    path('genres/', JanreViewSet.as_view({'get': 'list', 'post': 'create'}), name='janre_list'),
    path('genres/<int:pk>/', JanreViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='janre_detail'),

    path('movies/', MovieViewSet.as_view({'get': 'list', 'post': 'create'}), name='movie_list'),
    path('movies/<int:pk>/', MovieViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='movie_detail'),

    path('ratings/', RatingViewSet.as_view({'get': 'list', 'post': 'create'}), name='rating_list'),
    path('ratings/<int:pk>/', RatingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='rating_detail'),

    path('comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment_list'),
    path('comments/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='comment_detail'),
]
