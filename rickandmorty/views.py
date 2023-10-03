import requests

from django.shortcuts import render, HttpResponse
from .models import Character

# Create your views here.
def home_view(request):
    characters = Character.objects.all()
    context = {
        'characters': characters, 
    }
    return render(request, template_name='rickandmorty/home.html', context=context)

def get_rickmorty_data_view(request):

    url = "https://rickandmortyapi.com/api/character"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        results = data['results']
        for data in results:
            Character.objects.create(
                name=data['name'],
                status=data['status'],
                species=data['species'],
                gender=data['gender'],
                image=data['image'],
            )
        return HttpResponse('<h1>Data loaded correctly</h1>')
    else:
        return HttpResponse("<h1>Data didn't load correctly, please retry.</h1>")
    
def rick_game(request):
    return render(request, template_name='rickandmorty/game.html')