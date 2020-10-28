from django.urls import path
from .views import main_page, add_argonaute, reset_argonautes

urlpatterns = [
    # WildCodeSchool url
    path('home', main_page, name='home'),
    path('add', add_argonaute, name = "add-argonaute"),
    path('reset_argonautes', reset_argonautes, name = "reset-argonautes"),
]
