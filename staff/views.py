from django.urls import reverse_lazy

from staff.models import Staff
from django.views.generic import ListView, CreateView

from staff.forms import StaffForm


class ListStaffView(ListView):
    model = Staff
    template_name = "staff/list_staff.html"
    context_object_name = "staffs"


class CreateStaffView(CreateView):
    model = Staff
    form_class = StaffForm
    template_name = "staff/create_staff.html"
    success_url = reverse_lazy("staff_list")

