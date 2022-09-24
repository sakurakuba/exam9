from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from photo.forms import PhotoForm
from photo.models import Photo, Album


# Create your views here.
class IndexView(LoginRequiredMixin, ListView):
    model = Photo
    template_name = "photo/index.html"
    context_object_name = "photos"


class PhotoView(LoginRequiredMixin, DetailView):
    model = Photo
    template_name = 'photo/photo_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        u = self.request.user.groups.filter(name__in=['Moderators']).exists()
        context['u'] = u
        return context


class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'photo/photo_create.html'

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('photo:photo_view', kwargs={'pk': self.object.pk})


class PhotoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'photo/photo_update.html'
    permission_required = "photo.change_photo"

    def form_valid(self, form):
        response = super().form_valid(form)
        album = get_object_or_404(Album, pk=self.kwargs.get("pk"))
        self.object.album.add(album)
        return response

    def get_success_url(self):
        return reverse('photo:photo_view', kwargs={'pk': self.object.pk})

    def has_permission(self):
        return super().has_permission() or self.request.user.is_superuser or self.request.user


class PhotoDeleteView(PermissionRequiredMixin, DeleteView):
    model = Photo
    template_name = 'photo/photo_delete.html'
    success_url = reverse_lazy('photo:index')
    permission_required = "photo.delete_photo"

    def has_permission(self):
        return super().has_permission() or self.request.user.is_superuser or self.request.user

