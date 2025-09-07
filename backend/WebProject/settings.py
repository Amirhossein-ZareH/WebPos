"""
Django settings for ShopProject.
اتصال به SQL Server 2008 لوکال با Windows Authentication
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'replace-this-with-a-secure-key'
DEBUG = True
ALLOWED_HOSTS = []

# -----------------------------
# اپ‌ها
# -----------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # پکیج‌های جانبی
    'rest_framework',
    'corsheaders',

    # اپ‌های پروژه
    'tafzili',
    'product',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # برای CORS
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'WebProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'frontend'],
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

WSGI_APPLICATION = 'WebProject.wsgi.application'

# -----------------------------
# دیتابیس SQL Server 2008 با Windows Authentication
# -----------------------------
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'Shop',           # اسم دیتابیس
        'HOST': 'localhost',      # لوکال
        'PORT': '1433',           # پورت پیش‌فرض SQL Server
        'OPTIONS': {
            'driver': 'SQL Server Native Client 10.0',  # driver نصب شده روی سیستم
            'trusted_connection': 'yes',  # استفاده از Windows Authentication
        },
    }
}

# -----------------------------
# CORS
# -----------------------------
CORS_ALLOW_ALL_ORIGINS = True  # برای تست اولیه

# -----------------------------
# استاتیک
# -----------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'frontend']

# -----------------------------
# زبان و زمان
# -----------------------------
LANGUAGE_CODE = 'fa-ir'
TIME_ZONE = 'Asia/Tehran'
USE_I18N = True
USE_L10N = True
USE_TZ = True
