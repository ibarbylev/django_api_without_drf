from django.shortcuts import render

from django.http import JsonResponse
from django.views import View


def my_api_view(request):
    data = {
        'name': request.user.username,  # username of current logged-in user, otherwise Anonymous
        'url': 'https://www.pyscoop.com/',
        'skills': ['Python', 'Django'],
    }
    return JsonResponse(data)


class MyAPIView(View):
    def get(self, request):
        data = {
            'name': request.user.username,  # username of current logged-in user, otherwise Anonymous
            'url': 'https://www.pyscoop.com/',
            'skills': ['Python', 'Django'],
        }

        return JsonResponse(data)
