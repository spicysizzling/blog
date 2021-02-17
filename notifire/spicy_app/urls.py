from django.urls import path
from spicy_app import views

app_name = 'spicy_app'

urlpatterns = [
    path('recipe-page/', views.recipe, name='recipe'),
    
]
