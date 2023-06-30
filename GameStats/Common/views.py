from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "Common/home-page.html"


class NoAccessView(TemplateView):
    template_name = 'no_access.html'
