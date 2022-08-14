from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin
from rest_framework.decorators import action
from rest_framework import filters
from rest_framework import permissions
from rest_framework import status
from Blog_app.models import Post, Account
from .serializers import ImageSerializer, PostSerializer, PostCommentSerializer, AuthorSerializer


class ImageUploadView(CreateAPIView):
    serializer_class = ImageSerializer
    permission_classes = (permissions.IsAuthenticated,)

    # Созд объект с 2 мя полями на создаие имеджа
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ImegesView(ListAPIView):
    serializer_class = ImageSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.request.user.images.all()


class PostsViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, GenericViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    filterset_fields = ['author_id']
    serializer_class = PostSerializer

    def get_queryset(self):
        if self.action in ['update', 'partial_update']:
            return self.request.user.posts.all()
        return Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(methods=['post'], detail=True, url_path='add-comment')
    def add_comment(self, request, *args, **kwargs):
        post = self.get_object()
        serializer = PostCommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user, post=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=['post'], detail=True, url_path='like')
    def like(self, request, *args, **kwargs):
        post = self.get_object()
        post.likes.add(request.user)
        data = {'likes_amount': post.likes.count()}
        return Response(data, status=status.HTTP_201_CREATED)


class AuthorView(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AuthorSerializer


class DetailAuthorView(RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AuthorSerializer
