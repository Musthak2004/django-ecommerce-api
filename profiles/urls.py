from django.urls import path
from .views import ProfileDetailView, ProfileUpdateView

urlpatterns = [
    path("edit/", ProfileUpdateView.as_view(), name="profile_edit"),
    path("<slug:slug>/", ProfileDetailView.as_view(), name="profile_detail"),
]
