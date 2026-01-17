from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv
import os
import dj_database_url

# Load environment variables
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --- SECURITY CONFIGURATION ---

# 1. SECRET_KEY: Read from env or use fallback for local dev
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-local-dev-key')

# 2. DEBUG: False in Cloud (Render), True in Local
DEBUG = 'RENDER' not in os.environ

# 3. ALLOWED_HOSTS
ALLOWED_HOSTS = ['*']

# --- DATABASE CONFIGURATION ---
# Uses Neon (Cloud) if DATABASE_URL exists, otherwise Local SQLite
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# --- EMAIL CONFIGURATION ---
if 'RENDER' in os.environ:
    EMAIL_BACKEND = "anymail.backends.resend.EmailBackend"
    ANYMAIL = {
        "RESEND_API_KEY": os.environ.get('RESEND_API_KEY'),
    }
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# --- APPLICATION DEFINITION ---

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third Party
    'anymail',
    # Your Apps
    'apps.accounts',
    # Third Party
    'rest_framework',
    "rest_framework_simplejwt",
    'rest_framework_simplejwt.token_blacklist',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware", # For Render Static Files
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

# --- AUTH & PASSWORD ---

AUTH_USER_MODEL = 'accounts.User'  

AUTH_PASSWORD_VALIDATORS = [
    { "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator" },
    { "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator" },
    { "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator" },
    { "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator" },
]

# --- INTERNATIONALIZATION ---

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# --- STATIC FILES ---

STATIC_URL = "static/"
# CRITICAL FOR CLOUD: Tells Django where to put files when running collectstatic
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# --- REST FRAMEWORK & JWT ---

REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '50/day',
        'user': '500/day',
        'otp': '3/minute',
        'login': '5/minute',
    }
}

SIMPLE_JWT = { 
    'ACCESS_TOKEN_LIFETIME' : timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME' : timedelta(days=7),
    'ROTATE_REFRESH_TOKENS' : True,
    'BLACKLIST_AFTER_ROTATION' : True,
    'AUTH_HEADER_TYPES' : ('Bearer',),
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"