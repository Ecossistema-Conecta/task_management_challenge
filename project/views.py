import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, DetailView
from django.views.generic.list import ListView

from .forms import ProjectForm, TaskForm
from project.models import Project, Task


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["xValues4"] = ["Italy", "France", "Spain", "USA", "Argentina"]
        context["yValues4"] = [55, 49, 44, 24, 15]
        context["barColors4"] = ["#b91d47", "#00aba9", "#2b5797", "#e8c3b9", "#1e7145"]

        context["xValues3"] = ["Italy", "France", "Spain", "USA", "Argentina"]
        context["yValues3"] = [55, 49, 44, 24, 15]
        context["barColors3"] = ["red", "green", "blue", "orange", "brown"]

        context["xValues2"] = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
        context["yValues2"] = json.dumps([{
            'data': [860, 1140, 1060, 1060, 1070, 1110, 1330, 2210, 7830, 2478],
            'borderColor': "red",
            'fill': False
        }, {
            'data': [1600, 1700, 1700, 1900, 2000, 2700, 4000, 5000, 6000, 7000],
            'borderColor': "green",
            'fill': False
        }, {
            'data': [300, 700, 2000, 5000, 6000, 4000, 2000, 1000, 200, 100],
            'borderColor': "blue",
            'fill': False
        }])

        context["xValues1"] = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
        context["yValues1"] = [7, 8, 8, 9, 9, 9, 10, 11, 14, 14, 15]

        return context


class ListProjectView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "project/list_project.html"
    context_object_name = "projects"


class CreateProjectView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "project/create_project.html"
    success_url = reverse_lazy("project_list")


class DetailProjectView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "project/project_detail.html"
    context_object_name = "project"


class ListTaskView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "project/list_task.html"
    context_object_name = "tasks"
    kwargs = {"project": None}

    def get_queryset(self):
        project = self.kwargs.get("project")
        if project:
            return Task.objects.filter(project=project)
        return Task.objects.all()


class CreateTaskView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "project/create_task.html"

    def get_success_url(self):
        return reverse("task_list", kwargs={"project_id": self.kwargs["project_id"]})
