from django.contrib import admin
from app.models import Subject, UserGroup, UniversityUser


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(UserGroup)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(UniversityUser)
class UniversityUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username',)


