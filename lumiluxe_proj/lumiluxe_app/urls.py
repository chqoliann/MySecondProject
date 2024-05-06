from django.urls import path
from .views import index, signup_view, signin_view, logout_view, perfume_details, feedback_view, user_profile, like_perfume
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup_view, name='signup'),
    path('signin/', signin_view, name='signin'),
    path('logout/', logout_view, name='logout'),
    path('perfume_details/<int:perfume_id>/', perfume_details, name='perfume_details'),
    path('feedback/', feedback_view, name='feedback'),
    path('user/profile/', user_profile, name='user_profile'),
    path('like/<int:perfume_id>/', like_perfume, name='like_perfume'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
