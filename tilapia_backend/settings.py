# settings.py — FINAL PRODUCTION READY (Render + Railway)

from pathlib import Path
from datetime import timedelta
import os
from decouple import config
import dj_database_url

# ================= BASE =================
BASE_DIR = Path(__file__).resolve().parent.parent

# ================= SECURITY =================
SECRET_KEY = config('SECRET_KEY', default='django-insecure-temp-key')

DEBUG = config('DEBUG', default=False, cast=bool)

# ✅ SAFE + FLEXIBLE
ALLOWED_HOSTS = config(
ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS',
    default='localhost,127.0.0.1,web-production-04b0.up.railway.app,tilapia-hub.onrender.com',
    cast=lambda v: [s.strip() for s in v.split(',')]
)
# ================= APPS =================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',

    'auth_app',
    'marketplace_app',
    'calculator_app',
    'notifications_app',
    'tasks_app',
    'tilapia_backend',
]

# ================= MIDDLEWARE =================
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # 🔥 important
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ================= URL =================
ROOT_URLCONF = 'tilapia_backend.urls'
WSGI_APPLICATION = 'tilapia_backend.wsgi.application'

# ================= TEMPLATES =================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "frontend" / "build",  # ✅ FIXED (must match your folder)
        ],
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

# ================= DATABASE =================
DATABASES = {
    'default': dj_database_url.config(
        default=config(
            'DATABASE_URL',
            default=f'sqlite:///{BASE_DIR / "db.sqlite3"}'
        )
    )
}

# ================= AUTH =================
AUTH_USER_MODEL = 'auth_app.CustomUser'

# ================= PASSWORD VALIDATION =================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ================= INTERNATIONAL =================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ================= STATIC FILES =================
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "frontend" / "build" / "static",  # ✅ FIXED
]

STATIC_ROOT = BASE_DIR / "staticfiles"

# ✅ REQUIRED for production static serving
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ================= CORS =================
CORS_ALLOW_ALL_ORIGINS = True

# ================= REST FRAMEWORK =================
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# ================= JWT =================
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
}