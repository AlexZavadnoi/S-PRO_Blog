from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ImageUploadView, PostsViewSet, ImegesView, AuthorView, DetailAuthorView

app_name = 'api'
router = SimpleRouter()
router.register('posts', PostsViewSet, basename='posts')

urlpatterns = [
    path('upload-image/', ImageUploadView.as_view(), name='upload-image'),
    path('images/', ImegesView.as_view(), name='images'),
    path('authors/', AuthorView.as_view(), name='author'),
    path('authors/<int:pk>', DetailAuthorView.as_view(), name='detail-author'),
    path('', include(router.urls)),

]
