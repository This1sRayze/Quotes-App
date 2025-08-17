# Quotes App

A Django-based web application for managing and browsing famous quotes and authors.  
It allows users to explore, search, and organize quotes, while also supporting user management features.

## Features

* User registration, login, and password reset
* Create, edit, and delete quotes
- Import quotes/authors from JSON files.
* Django ORM with SQLite (default)
* Authentication system using Django's built-in auth
* Custom template tags and utilities
- Admin panel for managing users, quotes, and authors.
* HTML templates & CSS styling
* Ready for production deployment with Gunicorn + Nginx

## Project Structure
```
quotesapp/
│── manage.py               # Django management script
│── quotesapp/              # Main Django project settings
│   ├── settings.py         # Django settings
│   ├── urls.py             # Project URLs
│   ├── wsgi.py / asgi.py   # Deployment configs
│
├── quotes/                 # Quotes app
│   ├── models.py           # Quote & Author models
│   ├── views.py            # Business logic
│   ├── urls.py             # App routes
│   ├── admin.py            # Admin config
│   ├── utils.py            # Helper functions
│   └── templatetags/       # Custom Django template tags
│
├── users/                  # User management app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
└── utils/                  # Extra utilities & data
    ├── add_quotes.py       # Script to load quotes
    ├── migration.py        # Data migration helpers
    ├── authors.json        # Authors dataset
    └── quotes.json         # Quotes dataset
```

## Installation

1. Clone the repository  
   ```bash
   git clone https://github.com/yourusername/quotes-app.git
   cd quotes-app/quotesapp
   ```

2. Create & activate virtual environment  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate    # On Windows
   ```

3. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations  
   ```bash
   python manage.py migrate
   ```

5. Create superuser (for Django admin)  
   ```bash
   python manage.py createsuperuser
   ```

6. Load initial data (optional)  
   ```bash
   python manage.py shell < utils/add_quotes.py
   ```

7. Run development server  
   ```bash
   python manage.py runserver
   ```

## Usage

- Open the app in your browser: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
- Django Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Running Tests

The project includes unit tests inside each app (e.g., `accounts/tests.py`, `quotes/tests.py`).

Run tests with:

```bash
pytest
```

*(or `python manage.py test` if pytest isn’t configured)*


## Tech Stack

- **Backend:** Django 4.x  
- **Database:** SQLite (default), can be switched to PostgreSQL/MySQL  
- **Frontend:** Django Templates  
- **Data Import:** JSON utilities  


