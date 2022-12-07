from django.db import models
from django.urls import reverse
from users.models import CustomUser


class Healthy(models.Model):
    author = models.ForeignKey(CustomUser, related_name='author', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=250, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    Calories = models.IntegerField(null=True)
    
    
    def __str__(self):
        return self.title



    def get_absolute_url(self):
        return reverse('BeeHealthyApp:home', args=(self.pk,))




