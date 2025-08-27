from django.urls import path

from . import views

urlpatterns = [
    path("", views.room_page_view, name="room_list"),
    path("<int:pk>/", views.room_detail_view, name="room_detail"),
]
