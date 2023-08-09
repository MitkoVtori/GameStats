from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView
from GameStats.Common.forms import ReportProblemForm
from GameStats.Common.models import Problem


class HomePageView(TemplateView):
    template_name = "Common/home-page.html"


class NoAccessView(TemplateView):
    template_name = 'no_access.html'


class ReportProblemView(LoginRequiredMixin, CreateView):
    template_name = "Common/report-problem.html"
    form_class = ReportProblemForm
    success_url = reverse_lazy("problems")

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['creator'].initial = self.request.user.get_username()
        return form


class ProblemsView(LoginRequiredMixin, ListView):
    context_object_name = "problems"
    model = Problem
    template_name = "Common/problems.html"
