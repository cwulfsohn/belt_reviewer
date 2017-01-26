from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class InfoManager(models.Manager):
    def register(self, first_name, last_name, email, password, confirm_password):
        valid = []
        if len(first_name) < 2:
            valid.append('First Name does not match criteria')
            print 'length first name'

        if re.search(r'[0-9]',first_name):
            valid.append('First Name cannot contain numbers')
            print 'numbers first name'

        if len(last_name) < 2:
            valid.append('Last Name does not match criteria')
            print 'length last name'

        if re.search(r'[0-9]',last_name):
            valid.append('Last Name cannot contain numbers')
            print 'numbers last name'

        if len(email) < 2:
            valid.append('Email does not meet length requirement')

        if not email_regex.match(email):
            valid.append('Email does not fit criteria')

        if len(password) < 8:
            valid.append('Password does not meet length criteria')

        if password != confirm_password:
            valid.append('Password does not confirm')

        if len(valid) > 0:
            return (False, valid)
        try:
            hw_password = b''+str(password)
            hash_password = bcrypt.hashpw(hw_password, bcrypt.gensalt())
            register_info = Info(first_name = first_name, last_name = last_name, email = email, password = hash_password)
            register_info.save()
        except:
            valid.append('user already created')
        if len(valid)>0:
            return(False, valid)
        return True

    def login(self, email, password):
        error = []
        try:
            Info.objects.get(email = email)
        except:
            error.append('Email is invalid')
            return (False, error)
        user = Info.objects.get(email = email)
        if bcrypt.hashpw(password.encode(), user.password.encode()) == user.password:
            return True
        error = ['Password does not exist']
        return (False, error)


class Info(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    objects = InfoManager()
