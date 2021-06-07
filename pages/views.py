from typing import List
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Store
# Create your views here.


class HomePageView(ListView):
    model = Store
    template_name = 'home.html'
    context_object_name = 'stores'


class AboutPageView(ListView):
    model = Store
    template_name = 'about.html'
    context_object_name = 'stores'


class StorePageView(DetailView):
    model = Store
    template_name = 'store.html'
    context_object_name = 'store'

    def get_context_data(self, **kwargs):
        context = super(StorePageView, self).get_context_data(**kwargs)
        context['stores'] = Store.objects.all()
        return context
