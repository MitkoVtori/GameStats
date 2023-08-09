from django.urls import path
from GameStats.Common import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('access/denied/', views.NoAccessView.as_view(), name="no-access"),
    path('problems/', views.ProblemsView.as_view(), name="problems"),
    path('problems/report-problem/', views.ReportProblemView.as_view(), name='report-problem')
]