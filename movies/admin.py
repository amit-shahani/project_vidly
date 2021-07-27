from django.contrib import admin
from django.db import models
from .models import Cast, Genre, Movies, Actor

# Register your models here.


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
   # fields = ('title', 'genre') or
    list_display = ('title', "number_in_stock", 'daily_rate')
    exclude = ('date_created',)


class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'name')


# class CastAdmin(admin.ModelAdmin):

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movies, MovieAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Cast)
