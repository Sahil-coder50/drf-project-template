## Step 1: Create Template Repo

```bash
mkdir drf-project-template
cd drf-project-template
git init
```

## Step 2: Install Cookiecutter

```bash
sudo apt update
sudo apt install pipx
pipx ensurepath
pipx install cookiecutter
source ~/.bashrc
cookiecutter --version
```

## Step 3: Create Template Structure

### Structure
```text
drf-project-template
├── cookiecutter.json
└── {{cookiecutter.project_slug}}
    ├── apps
    │   └── __init__.py
    ├── common
    │   ├── __init__.py
    │   ├── exceptions
    │   │   ├── __init__.py
    │   │   ├── base.py
    │   │   ├── errors.py
    │   │   └── handlers.py
    │   ├── mixins
    │   │   └── __init__.py
    │   ├── pagination
    │   │   ├── __init__.py
    │   │   ├── standard_cursor_pagination.py
    │   │   └── standard_pagination.py
    │   ├── permissions
    │   │   └── __init__.py
    │   └── utils
    │       └── __init__.py
    ├── config
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings
    │   │   ├── __init__.py
    │   │   ├── base.py
    │   │   ├── local.py
    │   │   └── production.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── docker
    │   ├── Dockerfile
    │   └── docker-compose.yml
    ├── manage.py
    ├── media
    └── requirements
        ├── base.txt
        ├── local.txt
        └── production.txt

```
### Commands for making the Structure

```bash
mkdir -p "{{cookiecutter.project_slug}}"/{apps,common/{exceptions,mixins,pagination,permissions,utils},config/settings,docker,requirements} && \
touch cookiecutter.json "{{cookiecutter.project_slug}}"/{manage.py,.env,.gitignore,apps/__init__.py,common/__init__.py,common/exceptions/{__init__.py,base.py,errors.py,handlers.py},common/pagination/{__init__.py,standard_cursor_pagination.py,standard_pagination.py},common/mixins/__init__.py,common/permissions/__init__.py,common/utils/__init__.py,config/__init__.py,config/asgi.py,config/urls.py,config/wsgi.py,config/settings/{__init__.py,base.py,local.py,production.py},docker/{Dockerfile,docker-compose.yml},requirements/{base.txt,local.txt,production.txt}}
```

## Step 4: cookiecutter.json

```bash
{
  "project_name": "My Project",
  "project_slug": "my_project",
  "author": "your_name",
  "django_version": "4.2"
}
```

## Step 5: manage.py

```bash
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

```

## Step 6: Exceptions

### common/exceptions/handlers.py

```bash
import logging
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException

logger = logging.getLogger(__name__)
def custom_exception_handler(exc, context):
    # Call the default DRF exception handler first
    response = exception_handler(exc, context)
    # Log the exception with context
    logger.error(
        f"Exception: {exc.__class__.__name__} - {str(exc)}",
        extra={"request": context["request"], "view": context["view"]}
    )
    if response is not None:
        # Add more structured data to the response
        response.data = {
            "status_code": response.status_code,
            "error": response.data.get("detail", "An error occurred"),
            "exception": exc.__class__.__name__,
            "view": context["view"].__class__.__name__,
            "method": context["request"].method,
            "path": context["request"].path,
        }
    return response

```
## Step 7: Pagination

### common/pagination/standard_pagination.py

```bash
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class StandardPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            "status": "success",
            "pagination": {
                "total_records": self.page.paginator.count,
                "total_pages": self.page.paginator.num_pages,
                "current_page": self.page.number,
                "page_size": self.get_page_size(self.request),
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
            },
            "results": data,
        })

```

### common/pagination/standard_cursor_pagination.py

```bash
from rest_framework.pagination import CursorPagination
from rest_framework.response import Response

class StandardCursorPagination(CursorPagination):
    page_size = 20
    ordering = ("-created_at", "-id")

    def get_paginated_response(self, data):
        return Response({
            "status": "success",
            "pagination": {
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
            },
            'results': data,
        })

```

## Step 8: Settings

### settings/base.py

```bash
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
]

REST_FRAMEWORK = {
    "EXCEPTION_HANDLER":"common.exceptions.handlers.custom_exception_handler",
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

#Media files (user uploads)
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR,"media")

```

### settings/local.py

```bash
from .base import *

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

### settings/production.py

```bash
from .base import *

DEBUG = False

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS')

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}
```

## Step 9: urls.py

```bash
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]
```

## Step 10: Requirements Files

### requirements/base.txt
```bash
Django>=4.2
djangorestframework
psycopg2-binary
python-dotenv
```

### requirements/local.txt
```bash
-r base.txt
ipython
```

### requirements/production.txt
```bash
-r base.txt
gunicorn
```

## Step 11: .env File

```bash
SECRET_KEY=add_secret_key
ALLOWED_HOSTS=*

DB_ENGINE=django.db.backends.postgresql
DB_NAME=your_db_name
DB_USER=your_db_username
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

```

## Step 12: Docker Setup

### Dockerfile
```bash
FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements/base.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

### docker-compose.yml
```bash
version: "3.9"

services:
  web:
    build: .
    ports:
      - "8000:8000"
```

## Step 13: .gitignore

```bash
__pycache__/
.env
*.pyc
db.sqlite3
```

## Step 14: Commit and Push

```bash
git add .
git commit -m "Initial DRF project template"
git remote add origin https://github.com/your-username/drf-project-template.git
git branch -M main
git push -u origin main
```

## Step 15: Use to make Project Structure

### Use to make project structure
```bash
mkdir your_project
cd your_project
cookiecutter https://github.com/your-username/drf-project-template.git
```

### Use to add additional app in the project
```bash
cookiecutter https://github.com/your-username/drf-app-template.git
```
