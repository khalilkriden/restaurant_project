# Django Restaurant Project 🍽️

This is a restaurant management web application built using Django and MySQL.

## 🚀 Features

- User registration and login
- Admin login and Django admin panel
- CRUD operations for dishes (add, edit, delete)
- Dish categories (starter, main course, dessert)
- Search for dishes by name
- Pagination on menu page
- Table reservation system
- Upload dish images (ImageField)
- Success and error messages after actions
- Different redirection for Admin vs Normal User
- Bootstrap 5 responsive design
- MySQL database (connected via XAMPP)
- Clean Django Admin customization (list display, search, filter)

## 🛠️ Technologies Used

- Django 4+
- MySQL (via XAMPP)
- Bootstrap 5
- Pillow (for image uploads)
- mysqlclient (for Django-MySQL connection)

## 🖥️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/khalilkriden/restaurant_project.git
cd restaurant_project
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

- On **Windows PowerShell**:

```bash
.\.venv\Scripts\Activate.ps1
```

- On **Windows CMD**:

```bash
.\.venv\Scriptsctivate.bat
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your MySQL database

Open `restaurant_project/settings.py` and edit:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

Make sure your MySQL server (XAMPP) is running.

### 5. Run database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

### 8. Access the application

- Main Website: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Admin Panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

✅ Your project should now be running locally!

---

## 📜 License

This project is for educational purposes and personal portfolio use.

---

# 🎯 Notes

- Admin users are redirected automatically to `/admin/`
- Normal users are redirected to homepage `/`
- Success and error messages are displayed after every action
- Admin panel is customized with filters and search fields
- Bootstrap 5 is used for responsive design
- MySQL database is connected via XAMPP

---