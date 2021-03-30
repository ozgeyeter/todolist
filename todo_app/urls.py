from django.urls import path
from.import views



urlpatterns = [
    path('create', views.create, name='create'),
    path('', views.homepage, name='home'),
    path('about/', views.about, name='about'),]