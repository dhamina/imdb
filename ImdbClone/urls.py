from django.urls import path
from . import views

app_name = 'imdb'

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:type_no>/', views.detail, name='detail'),
    # path('detail', views.detail, name='detail'),
    path('search/', views.search, name='search'),
    path('register', views.register, name='register'),
    path('login', views.auth_login, name='login'),
    path("logout", views.logout_request, name= "logout"),
    ]