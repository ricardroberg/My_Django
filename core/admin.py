from django.contrib import admin
from .models import Learning, Knowledge, User, UserLogged

active_user = UserLogged

@admin.register(Knowledge)
class Knowledge(admin.ModelAdmin):
    list_display = ('active', 'knowledge', 'create', 'last_modified')

@admin.register(Learning)
class LearningAdmin(admin.ModelAdmin):
    list_display = ('active', 'learning', 'create', 'last_modified')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'create', 'last_modified')


