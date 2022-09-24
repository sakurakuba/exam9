from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from photo.forms import AlbumForm, PhotoAddForm
from photo.models import Album, Photo


class AlbumView(DetailView):
    template_name = 'album/album_view.html'
    model = Album

    def get_context_data(self, **kwargs):
        photo = get_object_or_404(Photo, pk=self.kwargs.get("pk"))
        context = super(AlbumView, self).get_context_data(**kwargs)
        context['photos'] = photo.album.all().order_by('-created_at')
        u = self.request.user.groups.filter(name__in=['Project Manager', 'Team Lead']).exists()
        context['u'] = u
        return context


class AlbumCreate(CreateView):
    form_class = AlbumForm
    template_name = "album/album_create.html"

    def form_valid(self, form):
        user = self.request.user
        form.instance.album_author = user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('photo:album_view', kwargs={'pk': self.object.pk})


class AlbumUpdate(UpdateView):
    template_name = 'album/album_update.html'
    form_class = AlbumForm
    model = Album

    def get_success_url(self):
        return reverse('photo:album_view', kwargs={'pk': self.object.pk})


class AlbumDelete(DeleteView):
    model = Album
    template_name = "album/album_delete.html"
    success_url = reverse_lazy("photo:index")


class PhotoAdd(UpdateView):
    model = Album
    form_class = PhotoAddForm
    template_name = "album/photos.html"

    def get_context_data(self, **kwargs):
        photos = Photo.objects.all()
        context = super().get_context_data(**kwargs)
        context['photos'] = photos.order_by('-created_at')
        u = self.request.user.groups.filter(name__in=['Project Manager', 'Team Lead']).exists()
        context['u'] = u
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        photo = get_object_or_404(Photo, pk=self.kwargs.get("pk"))
        self.object.photo.add(photo)
        return response

    def get_success_url(self):
        return reverse("photo:album_view", kwargs={"pk": self.object.pk})
