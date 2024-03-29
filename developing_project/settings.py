import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SESSION_COOKIE_SAMESITE = None

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hb!)rd6_wq$08g=u^kg!k#@mj&+g6y&#2(gznpc7t^vq-6lxdx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

<<<<<<< HEAD
ALLOWED_HOSTS = ['*']
=======

ALLOWED_HOSTS = ['*']

>>>>>>> b372cbee3ebc850d66aeeecb2c6b25ea7a7f2d4d


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'base.apps.BaseConfig'
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

ROOT_URLCONF = 'developing_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
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

WSGI_APPLICATION = 'developing_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'pDSy5qU9N6s63ypfEMjh',
        'HOST': 'containers-us-west-195.railway.app',
        'PORT': '5984',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'myproject',
#         'USER': 'ayyan',
#         'PASSWORD': 'yani1Mohar',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
#             'style': '{',
#         },
#         'simple': {
#             'format': '{levelname} {message}',
#             'style': '{',
#         },
#     },
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse',
#         }
#     },
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#         'file': {
#             'level': 'ERROR',
#             'class': 'logging.FileHandler',
#             'filename': 'debug.log',
#             'formatter': 'verbose'
#         },
#         'mail_admins': {
#             'level': 'ERROR',
#             'filters': ['require_debug_false'],
#             'class': 'django.utils.log.AdminEmailHandler',
#         },
#         'celerytask' : { # Specially define a log to collect specific information
#             'level' : 'INFO' ,
#             'class' : 'logging.handlers.RotatingFileHandler' , # Save to file , auto - cut
#             'filename' : os.path.join(BASE_DIR , "logs/app.log" ) ,
#             'maxBytes' : 1024 *1024* 50, # Log size 50M
#             'backupCount' : 5,
#             'formatter' : 'verbose',
#             'encoding' : "utf-8"
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console', 'file', 'mail_admins'],
#             # 'handlers': ['console','file',],
#             'level': os.getenv('DJANGO_LOG_LEVEL', 'ERROR'),
#             'propagate': True,
#         },
#         'django.request': {
#             'handlers': ['mail_admins'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#         'celerytask_log' : { # The logger named ' city'is also handled separately
#                 'handlers' : ['celerytask'] ,
#                 "propagate" : True ,
#                 'level' :  "INFO",
# },
#     },
# }


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
<<<<<<< HEAD
if DEBUG:
    STATICFILES_DIRS = [os.path.join(BASE_DIR,"static")]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
    
=======
STATICFILES_DIRS = [os.path.join(BASE_DIR,"static")]



STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')




>>>>>>> b372cbee3ebc850d66aeeecb2c6b25ea7a7f2d4d
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'


# CELERY_BROKER_URL = "redis://localhost:6379/"
# CELERY_TIMEZONE = 'UTC'
# CELERY_TASK_TRACK_STARTED = True
# SESSION_COOKIE_SAMESITE = None


<<<<<<< HEAD
EMIAL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587  
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
=======
# EMIAL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587  
# EMAIL_HOST_USER = ""
# EMAIL_HOST_PASSWORD = ""

>>>>>>> b372cbee3ebc850d66aeeecb2c6b25ea7a7f2d4d
