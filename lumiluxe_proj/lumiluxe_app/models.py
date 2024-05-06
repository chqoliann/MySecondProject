from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
class Brand(models.Model):
    brand_name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.brand_name


class Perfume(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    perfume_name = models.CharField(max_length=50)
    recipe = models.TextField()
    likes = models.IntegerField(default=0)
    image = models.ImageField(upload_to='perfume_images/')
    date = models.DateField()
    perfume_buy = models.URLField(blank=True)

    def __str__(self):
        return self.perfume_name


class FeedBackMessage(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField()
    message = models.TextField()
    date_sent = models.DateField()

    def __str__(self):
        return f"from {self.name} at {self.date_sent}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration_date = models.DateField(auto_now_add=True)
    liked_perfumes = models.ManyToManyField('Perfume', related_name='liked_by')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)