from django.urls import path
from . import views
appname="contact_list"
urlpatterns=[
    path('',views.home,name='home'),
    path('data/',views.data,name='data')
]