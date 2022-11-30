from django.urls import path
from . import views

app_name = 'BeeHealthyApp'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('create', views.CreatePost.as_view(), name='create'),
    path('create/<int:pk>/', views.Home.as_view(), name='home'),
]