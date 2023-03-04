from django.contrib import admin

from .models import *

admin.site.register(CustomUser)
admin.site.register(Tags)
admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Order)
