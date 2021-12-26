from django.urls import path

from .views import my_api_view, MyAPIView

urlpatterns = [
    path('awesome-api/', my_api_view),
    path('awesome-api-view-as-class/', MyAPIView.as_view()),
]
