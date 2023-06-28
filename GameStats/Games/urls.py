from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from GameStats.Games import views


urlpatterns = [
    path('create/', views.CreateGame.as_view(), name='create game')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)