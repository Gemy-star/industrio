from django.contrib import admin

# Register your models here.
from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import *


admin.site.register(WebsiteInfo, SingletonModelAdmin)

admin.site.register(Contact)

admin.site.register(Project)
