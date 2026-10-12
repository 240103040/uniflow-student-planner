from django.contrib import admin
from .models import Assignment

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ("title", "subject", "due_date", "is_completed")
    list_filter = ("is_completed", "subject")
    search_fields = ("title", "subject")
