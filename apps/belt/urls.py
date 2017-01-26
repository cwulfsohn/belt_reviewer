from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^show_review/$', views.show_review, name='show_review'),
    url(r'^show_book/$', views.show_book, name='show_book'),
    url(r'^add_review/$', views.add_review, name='add_review'),
    url(r'^add_another_review/$', views.add_another_review, name='add_another_review'),
    url(r'^users/(?P<id>\d+)$', views.users, name='users'),
    url(r'^show_book_again/(?P<title>.*)$', views.show_book_again, name='show_book_again'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),

]
