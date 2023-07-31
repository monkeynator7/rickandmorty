import requests

from django.shortcuts import render, HttpResponse
from .models import Character

# Create your views here.
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