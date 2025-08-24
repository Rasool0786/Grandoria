from django.contrib import admin

from .models import Room

@admin.register(Room)
class RoomAdminModel(admin.ModelAdmin):
    list_display = (
        "title",
        "price",
        "stars",
    )