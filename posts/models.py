from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(BaseModel):
    status = models.TextField()
    image = models.ImageField(upload_to="posts", null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user

    @property
    def get_all_comments(self):
        return self.comments.all()


class Like(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.user.username} liked post {self.post.pk}'
