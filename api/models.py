
# write
from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movies
from django.contrib.auth.models import User
from tastypie.authentication import BasicAuthentication


class MovieResource(ModelResource):
    class Meta:
        queryset = Movies.objects.all()
        resource_name = 'movies'
        excludes = ['date_created']
        authentication = BasicAuthentication()
