from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
class UserProfile(AbstractUser):
    name = models.CharField(blank=True, max_length=200)
    # USERNAME_FIELD = 'handle'
    # handle = models.CharField(blank=True, max_length=200, unique=True)
    # registeredDate = models.DateField(default=date.today)
    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('coders:user_info', kwargs={'username':self.username})

    class Meta:
        permissions = (("can_set_problems", "Required for setting problems"),)
