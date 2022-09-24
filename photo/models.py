from django.contrib.auth import get_user_model
from django.db import models


class Photo(models.Model):
    photo_img = models.ImageField(upload_to="photo_img", verbose_name="Photo Image")
    title = models.CharField(max_length=100, verbose_name='Title')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created date")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='photo_author',
                               verbose_name='Author')
    album = models.ManyToManyField("photo.Album", related_name="album", blank=True)
    private_photo = models.BooleanField(default=False, verbose_name="Private photo")

    def __str__(self):
        return f'{self.photo_img} - {self.title}, {self.author}'

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'


class Album(models.Model):
    name = models.TextField(max_length=50, verbose_name='Album name')
    description = models.TextField(max_length=1000, blank=True, null=True, verbose_name='Description')
    album_author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='album_author', verbose_name='Album Author')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created date")
    private_album = models.BooleanField(default=False, verbose_name="Private Album")

    def __str__(self):
        return f'{self.name} - {self.album_author}'

    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'
