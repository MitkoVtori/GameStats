from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from GameStats.Common.forms import ReportProblemForm, StaffChatForm
from GameStats.Common.models import Problem, StaffChat


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


class EditProblemView(LoginRequiredMixin, UpdateView):
    template_name = "Common/edit-problem.html"
    form_class = ReportProblemForm
    model = Problem
    context_object_name = "problem"
    success_url = reverse_lazy("problems")

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['creator'].initial = self.request.user.get_username()
        return form


class DeleteProblemView(LoginRequiredMixin, DeleteView):
    template_name = "Common/delete-problem.html"
    model = Problem
    context_object_name = "problem"
    success_url = reverse_lazy("problems")


class StaffChatView(LoginRequiredMixin, CreateView):
    template_name = "Common/staff-chat.html"
    form_class = StaffChatForm
    success_url = reverse_lazy("staff-chat")
    model = StaffChat
    context_object_name = "StaffChat"

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_staff and not self.request.user.is_superuser:
            return redirect("no-access")
        return super().get(request, *args, **kwargs)

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['creator'].initial = self.request.user.get_username()
        return form
