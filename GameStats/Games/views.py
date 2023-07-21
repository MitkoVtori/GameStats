from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from GameStats.Games.forms import GameForm, CommentGameForm, RateGameForm
from GameStats.Games.generators import game_rating_generator, next_comment_id_generator
from GameStats.Games.models import Game, Comment


class CreateGame(LoginRequiredMixin, CreateView):
    template_name = "Games/create-game.html"
    form_class = GameForm
    success_url = reverse_lazy('all-games')

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff and not request.user.is_superuser:
            return redirect("no-access")
        return super().get(request, *args, **kwargs)

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['creator'].initial = self.request.user.get_username()
        return form


class GamesView(ListView):
    template_name = "Games/all-games.html"
    model = Game
    context_object_name = "games"

    # Make sort logic


def game_details(request, pk):
    game = Game.objects.get(pk=pk)
    context = {
        "game": game,
        "rating": game_rating_generator(game.title)
    }
    return render(request, "Games/details.html", context)


@login_required
def comment_game(request, title):
    game = Game.objects.get(title=title)
    comment_creator = request.user

    comment_form = CommentGameForm(request.POST or None)
    rating_form = RateGameForm(request.POST or None)

    comment_form.fields["game"].initial = game.title
    rating_form.fields["game"].initial = game.title
    rating_form.fields["comment"].initial = next_comment_id_generator
    rating_form.fields["creator"].inital = comment_creator

    context = {
        "rating": rating_form,
        "comment": comment_form
    }

    if rating_form.is_valid() and comment_form.is_valid():
        rating_form.save()
        comment_form.save()
        return redirect("game-details", pk=game.id)

    return render(request, "Games/add-comment.html", context)

