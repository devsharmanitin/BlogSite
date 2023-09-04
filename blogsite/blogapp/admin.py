from django.contrib import admin

from .models import *


# Register your models here.



admin.site.register(blog)
admin.site.register(tag)
admin.site.register(Like)
admin.site.register(Comments)
admin.site.register(Contact)


