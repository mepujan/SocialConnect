from django.forms import ModelForm
from django import forms
from .models import Comment


class CommentForm(ModelForm):
    comment = forms.CharField(label="", max_length=200, widget=forms.TextInput(
        attrs={'placeholder': 'Comment'}))

    class Meta:
        model = Comment
        fields = ("comment",)
