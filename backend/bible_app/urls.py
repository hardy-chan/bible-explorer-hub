from django.urls import path
from .views import CleanSearchAPIView

urlpatterns = [
    path('search/', CleanSearchAPIView.as_view(), name='scripture-search'),
]
