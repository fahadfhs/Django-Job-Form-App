# from the django library
from django.urls import path
# views.py file here
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),  # added url pattern for about

]
