from django.urls import path
from .views import ProfileDetailView

urlpatterns = [
    path("<slug:slug>/", ProfileDetailView.as_view(), name="profile_detail"),
]
