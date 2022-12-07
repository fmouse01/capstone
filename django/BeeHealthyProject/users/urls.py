

from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('<str:username>/', views.ProfileView.as_view(), name='profile'),
    # path('<str:username>/edit', views.UpdateCalories.as_view(), name="update_daily_calories")
    path('updateProfile/<int:pk>',views.UpdateCalories.as_view(), name='updateProfile')
]