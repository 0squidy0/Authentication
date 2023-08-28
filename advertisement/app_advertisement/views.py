from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from .forms import AdvertForms
from .models import Advertisement
from django.contrib.auth import login, authenticate, logout

# Create your views here
def index(request):
    adverts = Advertisement.objects.all()
    context = {'adverts': adverts}
    return render(request, 'index.html', context)
def topSellers(request):
    return render(request, 'top-sellers.html')
def advertisementPost(request):
    if request.method == 'POST':
        form = AdvertForms(request.POST, request.FILES)
        if form.is_valid():
            advert = Advertisement(**form.cleaned_data)
            advert.user = request.user
            advert.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertForms()
    context = {'form': form}
    return render(request, 'advertisement-post.html', context)
def register(request):
    return render(request, 'register.html')
def login(request):
    # redirect_url = reverse('profile')
    # if request.method == 'GET':
    #     if request.user.is_authenticated:
    #         return redirect(redirect_url)
    #     else:
    #         return render(request, 'login.html')
    # username = request.POST('username')
    # password = request.POST('password')
    # user = authenticate(request, username=username, password=password)
    # if user is not None:
    #     login(request, user)
    #     return redirect(redirect_url)
    return render(request, 'login.html')


def profile(request):
    return render(request, 'profile.html')

def logout(request):
    #logout(request)
    return render(request, 'login.html')
def advertisement(request):
    return render(request, 'advertisement.html')

# def createAdv(request):
#     return render(request, 'advertisement-post.html')
