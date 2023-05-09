from django.contrib import admin
from .models import Resource, User, Category

# what you want to show up on the admin page
admin.site.register(Resource)
admin.site.register(User)
admin.site.register(Category)
