from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView
from GameStats.Games.models import Game
from GameStats.Profile.forms import AppUserCreationForm, LoginForm


class CreateUser(CreateView):
    template_name = "Profile/create-profile.html"
    form_class = AppUserCreationForm
    success_url = '/'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("home")

        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class UserLogin(LoginView):
    template_name = "Profile/login.html"
    form_class = LoginForm
    redirect_authenticated_user = True


class LogoutPageView(TemplateView):
    template_name = 'Profile/logout.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("home")
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class UserLogout(LogoutView):
    template_name = 'Profile/logout.html'


class UserDetails(LoginRequiredMixin, TemplateView):
    template_name = "Profile/details.html"

    def get_context_data(self, **kwargs):
        context = {
            "user": self.request.user,
            "games": Game.objects.filter(creator=self.request.user.get_username())
        }
        return context
