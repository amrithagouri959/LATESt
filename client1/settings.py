"""
Django settings for client1 project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j=+pj1%jfr!_%ewb14u=#uj4s@u(q8oxrw4r_tn03_tz3vuead'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# MIGHT BE UNSAFE BUT HERE WE GO 🔥
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
     'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'clientapp',
    'crispy_forms',
    'crispy_bootstrap5',
   

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

ROOT_URLCONF = 'client1.urls'

import os  # Make sure to import os at the top of your settings.py

# ... other settings

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'clientapp', 'templates')],  # Add your template directory here
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

# ... other settings

WSGI_APPLICATION = 'client1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# settings.py

import os

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Adjust the path as necessary
]


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ============================= CONFIGURATIONS ============================= #

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'

# ============================ CUSTOM VARIABLES ============================ #

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

TIME_ZONE = 'Asia/Kolkata'
USE_TZ = True
USE_L10N = True # Local time formatting

# settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.your_email_provider.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@domain.com'
EMAIL_HOST_PASSWORD = 'your_email_password'
JAZZMIN_SETTINGS = {
    "show_ui_builder": True,  # This can help visualize changes
    "theme": "flatly",  # Default theme for light mode
    "dark_mode_theme": "darkly",  # Dark theme
    "site_logo_classes": "img-circle",  # Optional styling for logos
     "site_brand": "TECH TOUCH",
     "copyright": "Technician",
    "site_logo": "clientapp/img/th (3).png", 
     
     "topmenu_links": [
        {"app": "clientapp"},
    ],

      "show_ui_builder": True,
}

JAZZMIN_UI_TWEAKS = {
     "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-light-lime",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "flatly",
    "dark_mode_theme": "superhero",
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    "dark_mode": True
}