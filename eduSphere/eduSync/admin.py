from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class userModel(UserAdmin):
    list_display = ['username', 'userType']

admin.site.register(customUser, userModel)