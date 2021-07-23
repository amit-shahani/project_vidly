from django.db import models
# write
from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movies


class MovieResource(ModelResource):
    class Meta:
        queryset = Movies.objects.all()
        resource_name = 'movies'
        excludes = ['date_created']
