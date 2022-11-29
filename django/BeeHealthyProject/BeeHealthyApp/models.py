from django.db import models
from django.urls import reverse
from users.models import CustomUser


class Healthy(models.Model):
    author = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True, null=True)
    
    
    def __str__(self):
        return self.title



    def get_absolute_url(self):
        return reverse('BeeHealthyApp:home', args=(self.pk,))

