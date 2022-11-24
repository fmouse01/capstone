from django.db import models
from django.urls import reverse
from users.models import CustomUser


# class Healthy(models.Model):
#     title = models.CharField(max_length=50)
#     author = models.ForeignKey(CustomUser, related_name='posts', on_delete=models.CASCADE, null=True)
#     body = models.TextField(max_length=200, null=True)
#     created = models.DateTimeField(auto_now_add=True, null=True)
    
    
#     def __str__(self):
#         return self.title
    
#     class Meta:
#         ordering = ['-created']


#     def get_absolute_url(self):
#         return reverse('BeeHealthyApp:home', args=(self.pk,))

