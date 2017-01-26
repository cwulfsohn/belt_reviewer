from __future__ import unicode_literals
from ..login.models import Info
from django.db import models

class BookManager(models.Manager):
    def home(self, email):
        name = Info.objects.get(email = email)
        return (name.first_name, name.id)
    def first_review(self, book, add_author, review, rating, email):
        name = Info.objects.get(email = email)
        author_name = Author.objects.create(name = add_author)
        book_name = Book.objects.create(title = book, author = author_name)
        Review.objects.create(review = review, rating = int(rating), book = book_name, users = name )
    def add_review(self, review, rating, book, email):
        book_name = Book.objects.get(title = book)
        name = Info.objects.get(email = email)
        Review.objects.create(review = review, rating = int(rating), book = book_name, users = name)


class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BookManager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, related_name='author_review')

    objects = BookManager()

class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(Book, related_name='book_review')
    users = models.ForeignKey(Info, related_name='user_review')

    objects = BookManager()
# Create your models here.
