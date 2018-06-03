from django.contrib import admin

# Register your models here.

from APP.models import BasicInfo, Marks

admin.site.register(BasicInfo)
admin.site.register(Marks)
