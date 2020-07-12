from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'user', 'date_created')
    list_filter = ('id', 'message', 'user', 'date_created')
    list_display_links = ('message',)

admin.site.register(Post, PostAdmin)
