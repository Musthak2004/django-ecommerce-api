from django.contrib.auth.forms import UserCreationForm as BaseCreationForm, UserChangeForm as BaseChangeForm
from .models import User

class UserCreationForm(BaseCreationForm):
    class Meta(BaseCreationForm.Meta):
        model = User
        fields = ("first_name", "last_name", "username", "email", "phone", "address")

class UserChangeForm(BaseChangeForm):
    class Meta(BaseChangeForm.Meta):
        model = User
        fields = ("first_name", "last_name", "username", "email", "phone", "address")