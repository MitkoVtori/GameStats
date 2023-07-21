from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from GameStats.Games import views


urlpatterns = [
    path('create/', views.CreateGame.as_view(), name='create game'),
    path('all/games/', views.GamesView.as_view(), name='all-games'),
    path('game/<int:pk>/details/', views.game_details, name='game-details'),
    path('game/<str:title>/comment/', views.comment_game, name='add-comment')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
