from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.views.generic import FormView
from django.views import View
from .forms import UserCreateForms


class RegisterFormView(FormView):
    form_class = UserCreateForms
    success_url = reverse_lazy('home')
    template_name = 'register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')
    template_name = 'login.html'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('home'))
