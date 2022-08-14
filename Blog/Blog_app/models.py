from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=50)
    subscribers = models.ManyToManyField('self', related_name='subscriptions')

    def __str__(self):
        return self.get_full_name()


class Post(models.Model):
    title = models.CharField(max_length=100)
    full_text = models.TextField()
    brief_text = models.CharField(max_length=50)
    author = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='posts')
    likes = models.ManyToManyField('Account', related_name='liked_posts')
    main_picture = models.ForeignKey('Image', on_delete=models.RESTRICT, related_name='main_picture_posts')
    additional_pictures = models.ManyToManyField('Image', related_name='additional_picture_posts', )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)


class PostComment(models.Model):
    text = models.TextField()
    author = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ('created_at',)


class Image(models.Model):
    picture = models.ImageField(upload_to='images')
    owner = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='images', null=True)

