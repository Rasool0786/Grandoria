from django.db import models
from django.urls import reverse


class Room(models.Model):
    STAR_CHOISES = (
        ("1", 1),
        ("2", 2),
        ("3", 3),
        ("4", 4),
        ("5", 5),
    )

    title = models.CharField(max_length=120)
    description = models.TextField()
    # ability -> ویژگی های اتاق
    price = models.PositiveIntegerField()
    stars = models.CharField(choices=STAR_CHOISES, max_length=1)
    picture = models.ImageField(upload_to="covers/", blank=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modifide = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("room_detail", kwargs={"pk": self.pk})
    