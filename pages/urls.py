from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    StorePageView,
    SearchResultsPageView,
    GroceryListPageView,
)

urlpatterns = [
    path('list/', GroceryListPageView.as_view(), name='list'),
    path('search/', SearchResultsPageView.as_view(), name='search_result'),
    path('store/<int:pk>', StorePageView.as_view(), name='store'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home')
]
