from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, ListView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from .models import Account, Post, Image
from .mixins import RequestUserMixin
from .forms import AccountForm


class HomeView(RequestUserMixin, ListView):
    model = Post
    context_object_name = 'posts_list'
    template_name = 'homePage.html'
    paginate_by = 10


class PostDetailView(RequestUserMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'


class ProfileView(RequestUserMixin, UpdateView):
    model = Account
    form_class = AccountForm
    success_url = reverse_lazy('home')
    template_name = 'profile.html'

    def get_object(self, queryset=None):
        return self.request.user


class ImageView(Image):
    # model = Image
    pass
