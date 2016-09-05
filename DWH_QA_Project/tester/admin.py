from django.contrib import admin
from .models import DataBase, Schema, Table
# Register your models here.

admin.site.register(DataBase)
admin.site.register(Schema)
admin.site.register(Table)
