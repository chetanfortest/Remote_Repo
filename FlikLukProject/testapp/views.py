from django.contrib.auth.decorators import login_required
from testapp.forms import SignUpForm
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from testapp.forms import AddMovieForm
from testapp.models import Movies

# Create your views here.

def index_page_view(request):
    return render(request, 'testapp/index.html')

@login_required
def home_page_view(request):
    movie = Movies.objects.all()
    return render(request, 'testapp/home.html', {'movie':movie})

@login_required
def kannada_page_view(request):
    movie = Movies.objects.filter(language='Kannada')
    return render(request, 'testapp/kannada.html', {'movie':movie})

@login_required
def hindi_page_view(request):
    movie = Movies.objects.filter(language='Hindi')
    return render(request, 'testapp/hindi.html', {'movie':movie})

@login_required
def telugu_page_view(request):
    movie = Movies.objects.filter(language='Telugu')
    return render(request, 'testapp/telugu.html', {'movie':movie})

@login_required
def addmovie_view(request):
    if request.method == 'POST':
        form = AddMovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = AddMovieForm()
    return render(request,"testapp/addmovie.html",{'form':form})


def logout_page_view(request):
    return render(request, 'testapp/logout.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'testapp/signup.html', {'form': form})
