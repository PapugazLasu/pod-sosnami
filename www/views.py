from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .models import Person
from django.contrib.auth.models import User
from .forms import PersonForm, LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    people = Person.objects.all()
    form = PersonForm()
    return render(request, 'index.html', {'people': people, 'form': form})

def detail(request, person_id):
    person = Person.objects.get(id=person_id)
    return render(request, 'detail.html', {'person': person})

def post_person(request):
    form = PersonForm(request.POST, request.FILES)
    if form.is_valid():
        person = form.save(commit = False)
        person.user = request.user
        person.saave()
    return HttpResponseRedirect('/')

def profile(request, username):
    user = User.objects.get(username=username)
    persons = Person.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'persons': persons})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponse("<h2>Konto jest wyłączone.</h2>")
            else:
                return HttpResponse("<h2>Błędne imię i/lub hasło.</h2>")
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')
        else:
            alert("Wypełnij formularz poprawnie!")
    else:
        form = UserCreationForm()
        return render(request, 'registration.html', {'form': form})

def like_person(request):
    person_id = request.POST.get('person_id', None)
    likes = 0
    if (person_id):
        person = Person.objects.get(id=int(person_id))
        if person is not None:
            likes = person.likes + 1
            person.likes = likes
            person.save()
    return HttpResponse(likes)

def search(request):
    search_val = request.GET.get('search', None)
    if (search_val != None):
        results = []
        persons = Person.objects.filter(name__icontains=search_val)
        for person in persons:
            json = {}
            json['name'] = person.name
            json['link'] = '/' + str(person.id) + '/'
            results.append(json)
        return JsonResponse({'results': results})
    else:
        return render(request, 'search.html')
