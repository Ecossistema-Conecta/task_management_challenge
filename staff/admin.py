from django.contrib import admin

from staff.models import Staff

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ["user", "group"]
    search_fields = ["user__username", "user__email"]
    list_filter = ["group"]
    ordering = ["user__username"]
    fieldsets = (
        (None, {"fields": ("user", "group")}),
    )
    add_fieldsets = (
        (None, {"fields": ("user", "group")}),
    )
    readonly_fields = ["user"]

