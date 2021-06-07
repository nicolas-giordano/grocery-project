from django.urls import path
from .views import HomePageView, AboutPageView, StorePageView

urlpatterns = [
    path('store/<int:pk>', StorePageView.as_view(), name='store'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home')
]
