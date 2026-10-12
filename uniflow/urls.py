from django.contrib import admin
from django.urls import path
from planner import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.dashboard, name="dashboard"),
    path("assignments/<int:assignment_id>/toggle/", views.toggle_assignment, name="toggle_assignment"),
]
