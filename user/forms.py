from django.forms import ModelForm
from .models import Profile


class UserUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email',
                  'address', 'bio', 'profile_pic')
