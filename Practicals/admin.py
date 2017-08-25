from django.contrib import admin

from .models import Subject, Practical

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject_name')

admin.site.register(Subject, SubjectAdmin)


@admin.register(Practical)
class PracticalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject')

