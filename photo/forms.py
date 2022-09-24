from django import forms
from django.forms import widgets

from photo.models import Photo, Album


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ("photo_img", "title", "album", "private_photo")
        widget = {"album": widgets.CheckboxSelectMultiple}


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ("name", "description", "private_album")


class PhotoAddForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ("photo",)
        widget = {"photo": widgets.CheckboxSelectMultiple}
