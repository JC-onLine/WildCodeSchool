from django.urls import path
from .views import main_page

urlpatterns = [
    # Activity url
    path('',
         main_page, name='main-page'),
]
