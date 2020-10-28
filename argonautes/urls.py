from django.urls import path
from .views import main_page, add_argonaute

urlpatterns = [
    # Activity url
    path('', main_page, name='main-page'),
    path('add', add_argonaute, name = "add-argonaute"),
]
