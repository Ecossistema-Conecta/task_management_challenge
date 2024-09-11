from django.urls import path

from .views import *

urlpatterns = [
    path('staff/', ListStaffView.as_view(), name='staff_list'),
    path('staff/create/', CreateStaffView.as_view(), name='staff_create'),
]
