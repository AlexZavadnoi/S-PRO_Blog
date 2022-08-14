from django.urls import path, include
from .views import HomeView, PostDetailView, ProfileView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', HomeView.as_view(), name='home'),
    path('posts/<pk>/', PostDetailView.as_view(), name='post_detail'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('api/', include('Blog_app.api.urls', namespace='api')),

]
