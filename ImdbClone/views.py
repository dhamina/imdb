from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm
from .models import Movie


def home(request):
    model = Movie
    movieData = Movie.objects.all()[:4]
    topRated = Movie.objects.all().filter(rating__gt=7.9)[:4]
    comingList = Movie.objects.all().filter(status='CS')[:4]
    inTheatreList = Movie.objects.all().filter(status='IT')[:4]
    context = {
        'movieList': movieData,
        'topList': topRated,
        'comingList': comingList,
        'inTheatreList': inTheatreList
    }
    print(topRated)
    return render(request, 'imdb_urls/home.html', context)


def detail(request, type_no):
    modelName = Movie
    print(type_no)
    details = Movie.objects.filter(id=type_no)
    context = {
        'details': details[0]
    }

    return render(request, 'imdb_urls/detail.html', context)


def search(request):
    query = request.GET.get('search')

    if query:
        results = Movie.objects.all().filter(title__icontains=query)
    else:
        results = []
    print(results)
    return render(request, 'imdb_urls/search.html', {'search': query, 'results': results})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registered Successfully')
            return redirect('imdb_urls:home')
            messages.error(request, 'Not able to Register. Invalid information')
    else:
        form = RegistrationForm()
    context = {'form': form}
    return render(request, 'imdb_urls/register.html', context)


def auth_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, "Successfully logged in")
                return redirect("imdb:home")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'imdb_urls/login.html', context)


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("imdb:home")
