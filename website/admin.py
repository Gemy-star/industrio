from django.contrib import admin

# Register your models here.
from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import WebsiteInfo


admin.site.register(WebsiteInfo, SingletonModelAdmin)