from django.urls import path
from .views import *
urlpatterns = [
    path('questions/<int:pk>',questions_api_view ),
    path('themes/',themes_api_view ),
]