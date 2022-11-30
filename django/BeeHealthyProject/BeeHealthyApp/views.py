from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .models import Healthy

# def myview(request):
#     context = {
#         'message': 'Hello World!'
#     }
#     return render(request, 'base.html', context)
    
    
class Home(ListView):
    model = Healthy
    template_name = 'home.html'


class CreatePost(LoginRequiredMixin, CreateView):
    model = Healthy
    template_name = 'create.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

