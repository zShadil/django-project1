from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("appointments/", include("appointments.urls")),
    path("", RedirectView.as_view(pattern_name="appointments:dashboard", permanent=False)),
]

# Serve static files in production (temporary workaround)
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
]

