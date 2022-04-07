from django.contrib import admin

# Register your models here.
from .models import Movie,Celebrity;

admin.site.register(Movie)
admin.site.register(Celebrity)
