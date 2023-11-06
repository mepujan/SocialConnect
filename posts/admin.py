from django.contrib import admin
from .models import Post, Like

admin.site.site_header = "Social Connect"
admin.site.site_title = "Social Connect Admin Portal"
admin.site.index_title = "Welcome to Social Connect  Portal"

admin.site.register(Post)
admin.site.register(Like)
