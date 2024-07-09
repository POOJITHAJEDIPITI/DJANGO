from django.urls import path
from . import views

urlpatterns=[
    path('validation/',views.validation,name='validation'),
    path('home_view/',views.home_view,name='home_view'),
    ]
