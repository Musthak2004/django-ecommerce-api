from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile

class ProfileDetailView(DetailView):
    model = Profile
    template_name = "profile_detail.html"
    context_object_name = "profile"
    slug_field = "slug"
    slug_url_kwarg = "slug"

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = "profile_edit.html"
    context_object_name = "profile"
    fields = ["bio", "profile_pic", "date_of_birth", "gender"]
    
    def get_object(self):
        return self.request.user.profile
    
    def get_success_url(self):
        return reverse_lazy("profile_detail", kwargs={"slug": self.object.slug})