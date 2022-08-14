from rest_framework import serializers
from Blog_app.models import Image, PostComment, Post, Account


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'picture',)
        read_only_fields = ('id',)


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'first_name', 'last_name',)


class PostCommentSerializer(serializers.ModelSerializer):
    author = AccountSerializer(read_only=True)

    class Meta:
        model = PostComment
        fields = ('id', 'text', 'author', 'created_at',)
        read_only_fields = ('id', 'created_at', 'author',)


class PostSerializer(serializers.ModelSerializer):
    author = AccountSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'full_text', 'brief_text', 'author', 'main_picture', 'additional_pictures',)
        read_only_fields = ('id', 'author',)
        # поиск по имени ????


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'first_name', 'last_name', 'birth_date', 'city',)
        read_only_fields = ('id',)
        # list posts ??
