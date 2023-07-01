from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from GameStats.Games.forms import GameForm


class CreateGame(LoginRequiredMixin, CreateView):
    template_name = "Games/create-game.html"
    form_class = GameForm
    success_url = '/'

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff and not request.user.is_superuser:
            return redirect("no-access")
        return super().get(request, *args, **kwargs)

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['creator'].initial = self.request.user.get_username()
        return form
