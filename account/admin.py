 
from django.contrib import admin
from django.conf import settings
from django.contrib.auth import get_user_model

from django.contrib.auth.admin import UserAdmin

admin.site.register(get_user_model(),UserAdmin)
