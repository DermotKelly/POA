from django.core.management.utils import get_random_secret_key
from pathlib import Path
import dj_database_url
import os

# Reset password via email.

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ['EMAIL_USER'] # Login email address, Stored as an environment varaible
EMAIL_HOST_PASSWORD = os.environ['EMAIL_PASS'] #App Password set from gmail, Stored as an environment varaible
#EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS') #App Password set from gmail, Stored as an environment varaible
#EMAIL_HOST_USER = os.environ.get('EMAIL_USER') # Login email address, Stored as an environment varaible


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('DJANOG_SECRET_KEY', get_random_secret_key())   

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


#os.getenv('DEBUG','False')
ALLOWED_HOSTS = ('127.0.0.1','localhost','poa-ngi7.onrender.com')


# Application definition

INSTALLED_APPS = [
    
    "blog.apps.BlogConfig",
    "users.apps.UsersConfig",
    'news.apps.NewsConfig',
    "crispy_forms", 
    "crispy_bootstrap5",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'magazine.apps.MagazineConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_project.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_project.wsgi.application'


# Database Setup

SECRET_KEY= os.environ.get('DJANGO_SECRET_KEY')
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///db.sqlite3')
DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}

# Password validation

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / 'staticfiles']
STATIC_ROOT = BASE_DIR / "static"



# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CRISPY_TEMPLATE_PACK = 'bootstrap5'
LOGIN_REDIRECT_URL = 'blog-home'
LOGIN_URL = 'login'
MEDIA_ROOT = BASE_DIR / "media" 
MEDIA_URL = '/media/'
