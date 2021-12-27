from django.urls import path

from .views import my_api_view, MyAPIView, BookView, BookView2

urlpatterns = [
    path('awesome-api/', my_api_view),
    path('awesome-api-view-as-class/', MyAPIView.as_view()),
    path('books/', BookView.as_view()),
    path('books-2/', BookView2.as_view()),
]
