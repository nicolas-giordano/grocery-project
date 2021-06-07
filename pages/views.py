from typing import List
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Store
# Create your views here.


class HomePageView(ListView):
    model = Store
    template_name = 'home.html'
    context_object_name = 'store_list'


class AboutPageView(ListView):
    model = Store
    template_name = 'about.html'
    context_object_name = 'store_list'
