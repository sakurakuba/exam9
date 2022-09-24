from django.urls import path

from photo.views.photo import IndexView, PhotoView, PhotoCreateView, PhotoUpdateView, PhotoDeleteView

app_name = "photo"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('photo/<int:pk>/', PhotoView.as_view(), name='photo_view'),
    path('photo/add/', PhotoCreateView.as_view(), name='photo_create'),
    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name='photo_update'),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo_delete'),
]
