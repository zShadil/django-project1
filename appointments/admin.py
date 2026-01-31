from django.contrib import admin

from .models import Doctor, Patient, Appointment


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("name", "specialty", "room_number")
    search_fields = ("name", "specialty")


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone")
    search_fields = ("full_name", "email", "phone")


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("patient", "doctor", "date", "time", "status")
    list_filter = ("status", "date", "doctor")
    search_fields = ("patient__full_name", "doctor__name", "reason")

