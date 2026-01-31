from django.urls import path

from . import views

app_name = "appointments"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("book/", views.book_appointment, name="book_appointment"),
    path("list/", views.appointment_list, name="appointment_list"),
]

