from django import forms

from .models import Appointment, Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["full_name", "email", "phone", "date_of_birth"]


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["doctor", "date", "time", "reason"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "time": forms.TimeInput(attrs={"type": "time"}),
        }

