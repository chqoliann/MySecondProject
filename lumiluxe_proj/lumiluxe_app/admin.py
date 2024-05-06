from django.contrib import admin
from .models import Perfume, Brand, FeedBackMessage, UserProfile

admin.site.register(Perfume)
admin.site.register(Brand)
admin.site.register(FeedBackMessage)
admin.site.register(UserProfile)
