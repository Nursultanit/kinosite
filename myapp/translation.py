from modeltranslation.translator import translator, TranslationOptions
from .models import Director, Actor, Movie

class DirectorTranslationOptions(TranslationOptions):
    fields = ('director_name', 'bio')

class ActorTranslationOptions(TranslationOptions):
    fields = ('actor_name', 'bio')

class MovieTranslationOptions(TranslationOptions):
    fields = ('movie_name', 'description')

translator.register(Director, DirectorTranslationOptions)
translator.register(Actor, ActorTranslationOptions)
translator.register(Movie, MovieTranslationOptions)
