from django.shortcuts import render, get_object_or_404


def room_page_view(request):
    return render(request, "rooms/room_list.html")


# def room_detail_view(request, pk):
#     room = get_object_or_404(Room, pk=pk)
#     return render(request, "rooms/room_detail.html", {"room": room})
