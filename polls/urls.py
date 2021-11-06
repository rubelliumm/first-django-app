from django.urls import path
from . import views



urlpatterns = [
    path('',views.polls,name='polls'),
    path('create/',views.create,name='create_poll'),
    path('vote/<pk>',views.vote,name='vote'),
    path('results/<pk>',views.results,name='polls_results'),
]
