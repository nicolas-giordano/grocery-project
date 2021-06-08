from typing import List
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Store, StoreItems
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['stores'] = Store.objects.all()
        return context


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


class SearchResultsPageView(ListView):
    model = StoreItems
    template_name = 'search_result.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        query = self.request.GET.get('query')
        return StoreItems.objects.filter(item__item__icontains=query)

    def get_context_data(self, **kwargs):
        context = super(SearchResultsPageView, self).get_context_data(**kwargs)
        context['stores'] = Store.objects.all()
        return context
