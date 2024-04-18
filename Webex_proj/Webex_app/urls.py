from django.urls import path
from .views import index, signup_view

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup_view, name='signup')
]
