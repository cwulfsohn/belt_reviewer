from django.shortcuts import render, redirect
from models import Info
from django.contrib import messages
from django.core.urlresolvers import reverse

def index(request):
    if 'valid' not in request.session:
        request.session['valid'] = []
    return render(request, 'login/index.html')

def register(request):
    if request.method == 'POST':
        register = Info.objects.register(request.POST['first_name'],request.POST['last_name'],request.POST['email'],request.POST['password'], request.POST['confirm_password'])
        if register == True:
            request.session['email'] = request.POST['email']
            print 'this works'
            return redirect(reverse('books:index'))
        messages_list = register[1]
        for errors in messages_list:
            messages.add_message(request, messages.INFO, errors)
        return redirect(reverse('login:my_index'))

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        login = Info.objects.login(email, password)
        if login == True:
            request.session['email'] = request.POST['email']
            print request.session['email']
            return redirect(reverse('books:index'))
        messages_list = login[1]
        for errors in messages_list:
            messages.add_message(request, messages.INFO, errors)
        return redirect(reverse('login:my_index'))

def success(request):
    return redirect(reverse('books:index'))

# Create your views here.
