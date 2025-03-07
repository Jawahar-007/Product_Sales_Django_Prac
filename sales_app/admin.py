from django.contrib import admin
from .models import Products , Orders , Blog , Comment
# Register your models here.

admin.site.register(Products) 
admin.site.register(Orders)
admin.site.register(Blog) 
admin.site.register(Comment) 
