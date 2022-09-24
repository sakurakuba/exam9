from django.urls import path

from photo.views import AlbumView, AlbumUpdate, AlbumDelete, AlbumCreate, PhotoAdd
from photo.views.photo import IndexView, PhotoView, PhotoCreateView, PhotoUpdateView, PhotoDeleteView

app_name = "photo"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('photo/<int:pk>/', PhotoView.as_view(), name='photo_view'),
    path('photo/add/', PhotoCreateView.as_view(), name='photo_create'),
    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name='photo_update'),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('album/<int:pk>/', AlbumView.as_view(), name="album_view"),
    path('album/<int:pk>/update', AlbumUpdate.as_view(), name="album_update"),
    path('album/<int:pk>/delete', AlbumDelete.as_view(), name="album_delete"),
    path('album/create/', AlbumCreate.as_view(), name="album_create"),
    path('album/<int:pk>/photo/add', PhotoAdd.as_view(), name="photo_add"),
]
