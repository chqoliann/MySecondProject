from django.contrib import admin
from django.urls import path
from .views import index, signup_view, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('signup/', signup_view, name='signup'),
    path('signin/', login, name='signin')
]
