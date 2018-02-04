from django.contrib import admin

# Register your models here.
from postings.models import BlogPost

admin.site.register(BlogPost)
