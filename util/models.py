from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

def post_user_created_signal(sender, instance, created, **kwargs):
    print ('sender - ', sender)
    print ('instance -', instance)
    print ('created -', created)
    print ('rest - ', kwargs)
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal, sender=User)
