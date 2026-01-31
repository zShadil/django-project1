from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("appointments/", include("appointments.urls")),
    path("", RedirectView.as_view(pattern_name="appointments:dashboard", permanent=False)),
]

