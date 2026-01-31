#!/usr/bin/env python
"""Quick script to add sample doctors to the database."""
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hospital_project.settings")
django.setup()

from appointments.models import Doctor

# Add sample doctors
doctors = [
    {"name": "Dr. Sarah Smith", "specialty": "Cardiology", "room_number": "101"},
    {"name": "Dr. John Williams", "specialty": "Pediatrics", "room_number": "202"},
    {"name": "Dr. Emily Davis", "specialty": "General Medicine", "room_number": "305"},
    {"name": "Dr. Michael Brown", "specialty": "Orthopedics", "room_number": "408"},
]

for doc_data in doctors:
    doctor, created = Doctor.objects.get_or_create(
        name=doc_data["name"],
        defaults={"specialty": doc_data["specialty"], "room_number": doc_data["room_number"]}
    )
    if created:
        print(f"[OK] Added: {doctor.name} ({doctor.specialty})")
    else:
        print(f"[EXISTS] Already exists: {doctor.name}")

print("\n[DONE] Refresh your booking page to see the doctors.")
