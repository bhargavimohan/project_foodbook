from django.contrib import admin
from .models import Recipe, Message

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'chef_name', 'chef_username', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'chef_name', 'chef_username')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'content', 'timestamp')
    search_fields = ('sender', 'receiver')

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Message, MessageAdmin)
