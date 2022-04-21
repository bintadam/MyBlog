from django.contrib import admin
from blogs.models import post
from blogs.models import Category

# Register your models here.
admin.site.register(post)
admin.site.register(Category)
