from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from pip._vendor import requests

from entertainment_db.models import Content


@login_required
def search_bar(request):
    if request.method == 'GET':
        search_word = request.GET['q']
        content = list()
        response = requests.get(f'http://www.omdbapi.com/?s={search_word}&apikey=329c0d5e').json()
        for data in response['Search']:
            content.append({"id": data['imdbID'], "name": data['Title'], "type": data['Type'], "img": data['Poster']})
        return JsonResponse({ "total_count": len(content), "items": content })
