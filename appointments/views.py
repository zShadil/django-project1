from django.db.models import Count
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import AppointmentForm, PatientForm
from .models import Appointment, Doctor


def dashboard(request):
    total_doctors = Doctor.objects.count()
    total_appointments = Appointment.objects.count()
    upcoming_appointments = (
        Appointment.objects.select_related("doctor", "patient")
        .order_by("date", "time")[:5]
    )

    top_doctors = (
        Doctor.objects.annotate(num_appointments=Count("appointments"))
        .order_by("-num_appointments")[:3]
    )

    context = {
        "total_doctors": total_doctors,
        "total_appointments": total_appointments,
        "upcoming_appointments": upcoming_appointments,
        "top_doctors": top_doctors,
    }
    return render(request, "appointments/dashboard.html", context)


def book_appointment(request):
    if request.method == "POST":
        patient_form = PatientForm(request.POST)
        appointment_form = AppointmentForm(request.POST)
        if patient_form.is_valid() and appointment_form.is_valid():
            patient = patient_form.save()
            appointment = appointment_form.save(commit=False)
            appointment.patient = patient
            appointment.save()
            return redirect(reverse("appointments:appointment_list"))
    else:
        patient_form = PatientForm()
        appointment_form = AppointmentForm()

    context = {
        "patient_form": patient_form,
        "appointment_form": appointment_form,
    }
    return render(request, "appointments/book_appointment.html", context)


def appointment_list(request):
    appointments = (
        Appointment.objects.select_related("doctor", "patient")
        .order_by("-date", "-time")
    )
    return render(request, "appointments/appointment_list.html", {"appointments": appointments})

