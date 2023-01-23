from django.contrib import admin

from Artist.models import User,Artist,Music

# Register your models here.
admin.site.register(User)
admin.site.register(Artist)
admin.site.register(Music)
