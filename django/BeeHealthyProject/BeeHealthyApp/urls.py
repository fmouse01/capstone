from django.urls import path
from . import views

app_name = 'BeeHealthyApp'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('create', views.CreatePost.as_view(), name='create'),
    path('create/<int:pk>/', views.Home.as_view(), name='home'),
    path('profile', views.Profile.as_view(), name='profile'),
    path('create/<int:pk>/edit', views.UpdateCalories.as_view(), name='update_calories')
]