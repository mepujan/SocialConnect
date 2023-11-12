from django.forms import ModelForm
from django import forms
from .models import Post


class PostForm(ModelForm):
    content = forms.CharField(
        label="Content", widget=forms.TextInput(attrs={'rows': 4}))

    class Meta:
        model = Post
        fields = ('content', 'image')
