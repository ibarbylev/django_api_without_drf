from django.shortcuts import render

from django.http import JsonResponse
from django.views import View
from .models import Book

from django.core.serializers import serialize  # import serializer from django

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


def my_api_view(request):
    data = {
        'name': request.user.username,  # username of current logged-in user, otherwise Anonymous
        'url': 'https://www.pyscoop.com/',
        'skills': ['Python', 'Django'],
    }
    return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class MyAPIView(View):
    def get(self, request):
        data = {
            'name': request.user.username,  # username of current logged-in user, otherwise Anonymous
            'url': 'https://www.pyscoop.com/',
            'skills': ['Python', 'Django'],
        }
        return JsonResponse(data)

    def post(self, request):
        data = {'message': 'This is a POST request'}
        return JsonResponse(data)

# class BookView(View):
#     def get(self, request):
#         books_count = Book.objects.count()  # TOTAL books in the database
#         books = Book.objects.all()  # Get all book objects from the database
#
#         data = {
#             'books': books,
#             'count': books_count,
#         }
#         return JsonResponse(data)


# ==== 1 Variant: Manually Serialize the object ======


@method_decorator(csrf_exempt, name='dispatch')
class BookView(View):
    def get(self, request):
        books_count = Book.objects.count()  # TOTAL books in the database
        books = Book.objects.all()  # Get all book objects from the database

        books_serialized_data = []  # to store serialized data
        for book in books:
            books_serialized_data.append({
                'book_title': book.title,
                'author_name': book.author,
                'book_price': book.price,
            })

        data = {
            'books': books_serialized_data,
            'count': books_count,
        }
        return JsonResponse(data)


# ==== 2 Variant: Using Inbuilt Serializer ======


class BookView2(View):
    def get(self, request):
        books_count = Book.objects.count()  # TOTAL books in the database
        books = Book.objects.all()  # Get all book objects from the database

        # Provide the serialize type such as python, json, xml, yaml, etc.
        # Here we are using 'python' because JsonResponse will automatically convert it to 'json'
        books_serialized_data = serialize('python', books)

        data = {
            'books': books_serialized_data,
            'count': books_count,
        }
        return JsonResponse(data)
