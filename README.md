# Hospital Appointment System (Django + SQLite)

This is a simple **Hospital Appointment System** built with **Django**, **SQLite**, and plain **HTML/CSS (Bootstrap)**.

It lets patients book appointments with doctors and lets staff view/manage upcoming appointments.

## 1. Prerequisites

- Python 3.10+ installed and on your PATH
- (Optional but recommended) A virtual environment

## 2. Setup

From the project root (`hospital` folder):

```bash
python -m venv .venv
.venv\Scripts\activate   # On Windows PowerShell: .venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

## 3. Django Commands

Apply migrations and create a superuser:

```bash
python manage.py migrate
python manage.py createsuperuser
```

Run the development server:

```bash
python manage.py runserver
```

Then open `http://127.0.0.1:8000/` in your browser.

## 4. Features

- List of doctors and specialties
- Simple patient information capture
- Appointment booking form (choose doctor, date, time, and reason)
- List of upcoming appointments
- Basic admin via Django admin

You can extend this with authentication, role-based dashboards (reception, doctor, admin), and more complex scheduling rules as needed.

