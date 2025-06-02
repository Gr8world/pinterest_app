# Pinterest Analytics Django Project

## Setup Instructions

1. Create a virtual environment and activate it.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Populate the `.env` file with:
   - `PINTEREST_ACCESS_TOKEN`
   - `SECRET_KEY`
   - `DEBUG`
   - `ALLOWED_HOSTS`
4. Apply migrations:
   ```
   python manage.py migrate
   ```
5. Run the development server:
   ```
   python manage.py runserver
   ```
6. Visit `http://localhost:8000/login/` to authenticate with Pinterest, then access the dashboard.

## Project Structure

- `config/` - Django project configuration (settings, URL, WSGI).
- `pinterest_app/` - Main app with views, services, templates, static files.
- `.env` - Environment variables.
- `requirements.txt` - Python dependencies.
- `manage.py` - Django management script.
