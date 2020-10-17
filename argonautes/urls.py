from django.urls import path
from .views import main_page, index, room

app_name = 'argonautes'


urlpatterns = [
    # path('', main_page, name='main-page'),
    path('', index, name='index'),
    path('<str:room_name>/', room, name='room'),
]
