from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Celebrity(User):
    # firstName = models.CharField(max_length=100)
    # lastName = models.CharField(max_length=200)
    ROLE_CHOICES = [
        ('Director', 'D'),
        ('Writer', 'W'),
        ('Star', 'S'),
    ]
    born_date = models.DateField(blank=True)
    city = models.CharField(blank=True, max_length=100)
    role = models.CharField(choices=ROLE_CHOICES, max_length=10)

    class Meta:
        verbose_name = 'Celebrity'


class Movie(models.Model):
    CATEGORY_CHOICES = [
        ('action', 'ACTION'),
        ('drama', 'DRAMA'),
        ('comedy', 'COMEDY'),
        ('romance', 'ROMANCE'),
        ('sci-fi', 'SCI-FI'),
        ('crime', 'CRIME'),
        ('Thriller', 'THRILLER'),
    ]

    STATUS_CHOICES = [
        ('RA', 'Recently Added'),
        ('MW', 'Most Watched'),
        ('TR', 'Top Rated'),
        ('IT', 'In Theatres'),
        ('CS', 'Coming Soon'),
    ]
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=1000)
    imageURL = models.TextField(max_length=10000)
    videoURL = models.TextField(max_length=10000)
    # image = models.ImageField(upload_to='movies')
    # banner = models.ImageField(upload_to='movies_banner')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    year = models.DateField()
    rating = models.DecimalField(max_digits=10, decimal_places=1)
    rating_count = models.IntegerField()
    # cast = models.ManyToManyField(Celebrity)

    def __str__(self):
        return self.title
