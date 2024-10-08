# Django-REST-framework-B

# Part-01

# Create the project directory

# cmd open

```
 mkdir Django_Rest_Framework

 cd Django_Rest_Framework
```

# Create a virtual environment to isolate our package dependencies locally

```
python -m venv myvenv  

```

# Mac use

// source emyvnv/bin/activate

# On Windows use

```
myvenv\Scripts\activate

```

# Install Django and Django REST framework into the virtual environment

```
pip install django

pip install pillow

pip install djangorestframework

pip install markdown

pip install django-filter

pip freeze > requirements.txt

pip install -r requirements.txt

pip uninstall -r requirements.txt -y

pip install -r requirements.txt

pip list

myvenv\Scripts\deactivate

```

# VS Code

```
code .
```

# Set up a new project with a single application

```
django-admin startproject My_Api

cd My_Api

python manage.py startapp status


```

# My_Api/Settings.py

```
INSTALLED_APPS = [
    'django.contrib.staticfiles',
    # Custom create
    'rest_framework',
    'status',

]

```

# My_Api/media/settings.py

```
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Custom create
MEDIA_DIR = BASE_DIR / 'media'

# Scroll down below
STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Media root directory => custom create
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'

```

# Than status/models.py

```
python manage.py migrate

python manage.py makemigrations status

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

```
# for Log erorr avoid than axios used
```
python -m pip install django-cors-headers

```
