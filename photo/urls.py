from django.urls import path

from photo.views import IndexView

app_name = "photo"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
]
