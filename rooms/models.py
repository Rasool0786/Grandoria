from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class Room(models.Model):
    STAR_CHOISES = (
        ("1", 1),
        ("2", 2),
        ("3", 3),
        ("4", 4),
        ("5", 5),
    )

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=120)
    stars = models.CharField(choices=STAR_CHOISES, max_length=1)
    description = models.TextField()
    # ability -> ویژگی های اتاق
    price = models.PositiveIntegerField()
    picture = models.ImageField(upload_to="covers/", blank=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modifide = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("room_detail", kwargs={"pk": self.pk})
    
def upload_to_path(instance, filename):
    room_title_slug = slugify(instance.room.title)
    return f"rooms/{room_title_slug}/{filename}"

class ImageMulti(models.Model):
    author = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE, 
        related_name="image", 
        verbose_name=_("Author"), 
        null=True
        )
    room = models.ForeignKey(
        Room, 
        on_delete=models.CASCADE, 
        related_name="image", 
        null=True
        )
    images = models.ImageField(
        upload_to=upload_to_path, 
        blank=True,
        )
    active = models.BooleanField(default=True)
    
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modifide = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.author)
    
    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         current_count = ImageMulti.objects.filter(
    #             room=self.room, 
    #             active=True
    #         ).count()
    #         if current_count >= 4:
    #             raise ValidationError(
    #                 "شما نمی‌توانید بیشتر از ۴ عکس برای این اتاق آپلود کنید. (به جز کاور اصلی)"
    #             )
    #     super().save(*args, **kwargs)
        