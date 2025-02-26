import os
from pathlib import Path
import json
import socket
if socket.gethostname()=="candr3w":
    print("hello")
#This is because the ebay redirects require https but the server only supports HTTP
   # SESSION_COOKIE_SECURE = True
   # CSRF_COOKIE_SECURE = True
   # SECURE_SSL_REDIRECT = True
   # SESSION_COOKIE_SECURE = False
   # CSRF_COOKIE_SECURE = False
   # SECURE_SSL_REDIRECT = False


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
# print(os.path.join(BASE_DIR, 'home/templates'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
PROJECT_NAME = "backend"
CONFIG = json.load(open(f"{BASE_DIR}/config.json"))
SECRET_KEY = CONFIG['Django']['DJANGO_SECRET_KEY']


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [

    "local.host",
    "localhost",
    "192.168.4.178",
    "127.0.0.1"

]


# Application definition

INSTALLED_APPS = [
    "accounts.apps.AccountsConfig",
    "api.apps.ApiConfig",

#    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    #'allauth.account.auth_backends.AuthenticationBackend',
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    # 'livereload.middleware.LiveReloadScript',
    #"allauth.account.middleware.AccountMiddleware",
]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    }
}
#CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
#CRISPY_TEMPLATE_PACK = "bootstrap4"

# ACCOUNT_FORMS = {
#    'signup': 'User.forms.SignUpForm'
# }
#ACCOUNT_EMAIL_REQUIRED = True
#ACCOUNT_USERNAME_REQUIRED = True
#ACCOUNT_SESSION_REMEMBER = True
#ACCOUNT_AUTHENTICATION_METHOD = 'email'
#ACCOUNT_UNIQUE_EMAIL = True
#ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'
#ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
#


CORS_ALLOW_ALL_ORIGINS = True
#CORS_ALLOWED_ORIGINS = [
#    'http://localhost:3000',  # Allow requests from your React frontend
#    # Add more origins as needed
#]
CORS_ALLOW_CREDENTIALS = True
CSRF_COOKIE_SECURE = False
#CSRF_COOKIE_NAME = 'csrftoken'  # Name of the CSRF token cookie
#CSRF_COOKIE_PATH = '/'           # Path of the CSRF token cookie
#CSRF_COOKIE_SECURE = True       # Whether the CSRF token cookie should only be sent over HTTPS
#CSRF_COOKIE_HTTPONLY = True     # Whether the CSRF token cookie should be accessible only via HTTP (not JavaScript)
#CSRF_COOKIE_SAMESITE = 'Lax'    # SameSite attribute for the CSRF token cookie (e.g., 'Strict', 'Lax', 'None')
CSRF_TRUSTED_ORIGINS = ['http://localhost:3000', "http://127.0.0.1:8000"]
ROOT_URLCONF = f"{PROJECT_NAME}.urls"

print(os.path.join(BASE_DIR, 'frontend', 'build'))
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, f'{PROJECT_NAME}/templates'),
            os.path.join(BASE_DIR, 'frontend', 'build'),
            os.path.join(BASE_DIR, 'frontend', 'public'),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            'libraries':{
#                'pagination_filters': f'{PROJECT_NAME}.templatetags.pagination_filters',
            },
            'builtins': ['django.templatetags.static'],
        },
    },
]

WSGI_APPLICATION = f"{PROJECT_NAME}.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "OPTIONS": CONFIG["Database"]

    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
print(os.path.join(BASE_DIR, f'{PROJECT_NAME}/static'))
if DEBUG:
    STATICFILES_DIRS = [
        #os.path.join(BASE_DIR, f'{PROJECT_NAME}/templates'),
        #os.path.join(BASE_DIR, 'frontend', 'build', 'static'),  # Path to React app's static files
        # os.path.join(BASE_DIR, f'{PROJECT_NAME}/static'),
        ('react', os.path.join(BASE_DIR, 'frontend', 'build', 'static')),
    ]
else:
    STATICFILES_DIRS = [
        # Production static files configuration
        os.path.join(BASE_DIR, 'static'),  # Path to your static files directory
    ]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
