from django.urls import path

from .views import my_api_view

urlpatterns = [
    path('awesome-api/', my_api_view),
]
