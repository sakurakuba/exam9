from django.urls import path


app_name = "photo"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
]
