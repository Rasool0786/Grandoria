from django.contrib import admin

from .models import Room, ImageMulti
from .forms import ImageMultiForm


class ImageMultisInline(admin.TabularInline):
    model = ImageMulti
    form = ImageMultiForm
    fields = (
        "author",
        "images",
        "active",
    )
    extra = 1
    max_num = 5
    


@admin.register(Room)
class RoomAdminModel(admin.ModelAdmin):
    list_display = (
        "title",
        "price",
        "stars",
        "datetime_modifide",
    )
    inlines = [
        ImageMultisInline,
    ]

@admin.register(ImageMulti)
class ImageMultiAdminModel(admin.ModelAdmin):
    form = ImageMultiForm
    list_display = (
        "author",
        "room",
        "datetime_modifide",
    )