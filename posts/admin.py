from django.contrib import admin

from .models import  comment, post


admin.site.register(post)
admin.site.register(comment)
