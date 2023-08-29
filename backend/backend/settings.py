from pathlib import Path

from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-8@)lb**bgzkp3ya5ym0!0%91icfco61c-zore57%1!3p^+nhzu'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',

    'djoser',

    'drf_spectacular',

    'api.apps.ApiConfig',
    'users.apps.UsersConfig'
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

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",

    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]

ROOT_URLCONF = 'backend.urls'

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

WSGI_APPLICATION = 'backend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
           'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

DJOSER = {
       'LOGIN_FIELD': 'email',
       'USER_CREATE_PASSWORD_RETYPE': True,
       'HIDE_USERS': False,
       'ACTIVATION_URL': 'activate/{uid}/{token}',
       'PASSWORD_RESET_CONFIRM_URL': 'users/set_password/{uid}/{token}',
       'SERIALIZERS': {
           'user_create':
               'api.users.users_serializers.UserCreateSerializer',
           'user':
               'api.users.users_serializers.CustomUserSerializer',
           'user_delete':
               'djoser.serializers.UserDeleteSerializer',
           'current_user':
               'api.users.users_serializers.CustomUserSerializer',
           'set_password':
               'djoser.serializers.SetPasswordSerializer',
           'set_password_retype':
               'djoser.serializers.SetPasswordRetypeSerializer',
           'token': 'djoser.serializers.TokenSerializer',
           'token_create': 'djoser.serializers.TokenCreateSerializer',
       },
       'PERMISSIONS': {
           'user': ('rest_framework.permissions.IsAuthenticated',),
           'user_list': ('rest_framework.permissions.AllowAny',),
       },
   }

AUTH_USER_MODEL = 'users.User'


MAX_LENGTH_EMAIL = 254
MAX_LENGTH_USERNAME = 150
MIN_LENGTH_PASSWORD = 6
MAX_LENGTH_PASSWORD = 30


SPECTACULAR_SETTINGS = {
    'TITLE': 'Longevity API',
    'DESCRIPTION': 'API documentation for my project',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': True,
    'SWAGGER_UI_SETTINGS': {
        'filter': True,
        'deepLinking': False,
        'persistAuthorization': False,
        'displayOperationId': True,
        'defaultModelsExpandDepth': -1,
        'defaultModelExpandDepth': 3,
        'docExpansion': 'none',
        'tagsSorter': 'alpha',
        'operationsSorter': 'alpha',
        'exampleValueCode': True,
    },
    'COMPONENT_SPLIT_REQUEST': True,
    'EXAMPLES_PROVIDE_MEDIA_TYPE': True,
    'EXAMPLES_SETTINGS': {
        'mediaTypes': {
            'application/json': {
                'example': '{"key": "value"}',
            },
        },
    },
}
