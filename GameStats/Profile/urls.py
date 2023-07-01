from django.urls import path
from GameStats.Profile import views


urlpatterns = [
    path('register/', views.CreateUser.as_view(), name="register"),
    path('login/', views.UserLogin.as_view(), name="login"),
    path('@me/logout/', views.LogoutPageView.as_view(), name='logout'),
    path('@me/logout/action/', views.UserLogout.as_view(), name='logout-action'),
    path('@me/', views.UserDetails.as_view(), name='user')
]
