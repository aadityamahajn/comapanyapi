# Django Rest Framework API Project

This is a simple REST API built using Django and Django Rest Framework (DRF)

## 🚀 Quick Start Guide

Follow these steps to get the project running on your local machine.

### 1. Clone the Project
Open your terminal/bash and run:
`git clone https://github.com/aadityamahajn/comapanyapi`
`cd Companyapi`

### 2. Setup Environment & Installation
Create virtual environment
`python -m venv venv`

Activate virtual environment
*On Windows:*
`source venv/Scripts/activate`
*On Mac/Linux:*
`source venv/bin/activate`

**Install Django and DRF**
`pip install django djangorestframework`

### 3. Database Migrations
Initialize the database and create the necessary tables:
`python manage.py makemigrations`
`python manage.py migrate`

### 4. Create Superuser (Optional)
To access the Django Admin panel, create an admin account:
`python manage.py createsuperuser`

### 5. Run the Server
`python manage.py runserver`
The API will now be live at: `http://127.0.0.1:8000/`
