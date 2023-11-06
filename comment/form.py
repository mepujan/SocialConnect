from django.forms import ModalForm
from .models import Comment


class CommentForm(ModalForm):
    class Meta:
        model = Comment
        fields = ("comment",)
