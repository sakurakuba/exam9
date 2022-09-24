from django.contrib.auth import authenticate, login, logout, get_user_model, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView
from accounts.forms import MyUserCreationForm, UserChangeForm

User = get_user_model()


class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "profile.html"
    context_object_name = "user_obj"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class RegisterView(CreateView):
    model = User
    template_name = 'registration.html'
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('review:index')
        return next_url


def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('review:index')
        else:
            context['has_error'] = True
    return render(request, 'login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('review:index')


class ChangeProfileView(PermissionRequiredMixin, UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = "change_user.html"
    context_object_name = "user_obj"

    def has_permission(self):
        return self.request.user.is_superuser or self.request.user == self.get_object()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(instance=self.object, data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return redirect("accounts:profile", self.object.pk)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class ChangePasswordView(PasswordChangeView):
    template_name = "change_password.html"

    def get_success_url(self):
        return reverse("accounts:profile", kwargs={"pk": self.request.user.pk})



