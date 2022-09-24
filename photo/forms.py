from django import forms
from photo.models import Photo, Album


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ("photo_img", "title", "album", "private_photo")


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ("name", "description", "private_album")
