from django.contrib import admin
from xunjiansys.models import Equipment, Floor, Location_type, Record

# Register your models here.
admin.site.register(Equipment)

admin.site.register(Record)

admin.site.register(Floor)

admin.site.register(Location_type)
