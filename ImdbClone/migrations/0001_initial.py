# Generated by Django 4.0.3 on 2022-04-06 17:17

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Celebrity',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('born_date', models.DateField(blank=True)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('role', models.CharField(choices=[('Director', 'D'), ('Writer', 'W'), ('Star', 'S')], max_length=10)),
            ],
            options={
                'verbose_name': 'Celebrity',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=1000)),
                ('imageURL', models.TextField(max_length=10000)),
                ('videoURL', models.TextField(max_length=10000)),
                ('category', models.CharField(choices=[('action', 'ACTION'), ('drama', 'DRAMA'), ('comedy', 'COMEDY'), ('romance', 'ROMANCE'), ('sci-fi', 'SCI-FI'), ('crime', 'CRIME'), ('Thriller', 'THRILLER')], max_length=10)),
                ('status', models.CharField(choices=[('RA', 'Recently Added'), ('MW', 'Most Watched'), ('TR', 'Top Rated'), ('IT', 'In Theatres'), ('CS', 'Coming Soon')], max_length=2)),
                ('year', models.DateField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=10)),
                ('rating_count', models.IntegerField()),
                ('cast', models.ManyToManyField(to='ImdbClone.celebrity')),
            ],
        ),
    ]
