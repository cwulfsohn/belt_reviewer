from django.shortcuts import render, redirect
from .models import *
from ..login.models import Info
from django.core.urlresolvers import reverse

def index(request):
    email = request.session['email']
    first_name = Review.objects.home(email)
    request.session['id'] = first_name[1]
    top_3_books = Review.objects.filter(users__email=email).order_by('-created_at')[:3]
    all_books = Review.objects.all()
    context = {
        'first_name':first_name[0],
        'top_3_books':top_3_books,
        'all_books':all_books,
    }
    return render(request, 'belt/index.html',context)

def show_review(request):
    author_name = Author.objects.all()
    context = {
        'author_name':author_name
    }
    return render(request, 'belt/review.html', context)

def add_review(request):
    if request.method == 'POST':
        book_name = request.POST['book_title']
        if len(request.POST['add_author']) > 0:
            add_author = request.POST['add_author']
        elif request.POST['list_author']== 'no':
            print request.POST['list_author']
            return redirect(reverse('books:show_review'))
        else:
            print request.POST['list_author']
            add_author = request.POST['list_author']
        review = request.POST['review']
        rating = request.POST['rating']
        request.session['book'] =  book_name
        email = request.session['email']
        print email
        add_book_to_db = Book.objects.first_review(book_name, add_author, review, rating, email)
    return redirect(reverse('books:show_book'))

def add_another_review(request):
    if request.method == 'POST':
        review = request.POST['review']
        rating = request.POST['rating']
        book_name = request.session['book']
        email = request.session['email']
        review_to_db = Review.objects.add_review(review, rating, book_name, email)
    return redirect(reverse('books:show_book'))

def show_book(request):
    book_title = request.session['book']
    book_info = Author.objects.filter(author_review__title = book_title)
    review_info = Review.objects.filter(book__title = book_title)
    context = {
        'book_info':book_info,
        'review_info': review_info
    }
    return render(request, 'belt/book_review.html', context)

def users(request, id):
    count = 0
    books = []
    user_info = Info.objects.get(id = id)
    email_name = user_info.email
    review_info = Review.objects.filter(users__email = email_name)
    for reviews in review_info:
        count += 1
        books.append(reviews.book.title)
    context = {
        'user_info': user_info,
        'review_info': count,
        'book_info': books
    }
    return render(request, 'belt/user.html', context)

def show_book_again(request, title):
    request.session['book'] = title
    return redirect(reverse('books:show_book'))

def delete(request, id):
    delete_data = Review(id = id)
    delete_data.delete()
    return redirect(reverse('books:show_book'))

def logout(request):
    request.session.clear
    return redirect(reverse('login:my_index'))

# Create your views here.
