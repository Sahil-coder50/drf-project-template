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

```bash
```
drf-project-template
├── README.md
├── cookiecutter.json
└── {{cookiecutter.project_slug}}
    ├── apps
    │   └── __init__.py
    ├── common
    │   ├── __init__.py
    │   ├── pagination
    │   │   └── __init__.py
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
    └── requirements
        ├── base.txt
        ├── local.txt
        └── production.txt

```
```

