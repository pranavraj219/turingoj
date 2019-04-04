from django.contrib import admin
from coders.models import UserProfile
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserProfile, UserProfileAdmin)
