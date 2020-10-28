from django.urls import path
from .views import main_page, add_argonaute

urlpatterns = [
    # WildCodeSchool url
    path('home', main_page, name='home'),
    path('add', add_argonaute, name = "add-argonaute"),
]
