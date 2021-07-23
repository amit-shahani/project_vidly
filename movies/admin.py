from django.contrib import admin
from .models import Genre, Movies

# Register your models here.


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
   # fields = ('title', 'genre') or
    list_display = ('title', "number_in_stock", 'daily_rate')
    exclude = ('date_created',)


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movies, MovieAdmin)