from rest_framework import generics

from .models import Book

from .serializers import BookSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class BookCreate(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['author']  # Add fields you want to filter by
    search_fields = ['title']      # Add fields you want to search by


# Retrieve a book by ID
class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Update a book by ID
class BookUpdate(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Delete a book by ID
class BookDelete(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
