from django.urls import path
from . import views

app_name = 'BeeHealthyApp'
urlpatterns = [
    path('', views.myview, name='home'),
]