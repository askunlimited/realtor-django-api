from django.urls import path
from .views import RealtorListView, RealtorDetailView, TopSellerView


urlpatterns = [
    path('', RealtorListView.as_view(), name='list'),
    path('topseller/', TopSellerView.as_view(), name='top-seller'),
    path('<pk>', RealtorDetailView.as_view(), name='detail'),
    
]