from django.urls import path
from sponsors.views import SponsorListAPIView


urlpatterns = [
    path('sponsors/', SponsorListAPIView.as_view(), name='sponsors-list')
]