"""
Django settings for cms_dashboard project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*js49e-9i#pg44&o!rcz&b0t#(^^0-)%prl!418b3je7!mm+%g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'cms_dashboard.urls'

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

WSGI_APPLICATION = 'cms_dashboard.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# dashboards
DASHBOARD_URL_NAMES = {
    'employee_dashboard_url': 'cms_dashboard:employee_dashboard_url',
    'employee_listboard_url': 'cms_dashboard:employee_listboard_url',
    'emp_contract_listboard_url': 'cms_dashboard:emp_contract_listboard_url',
    'pi_contract_listboard_url': 'cms_dashboard:pi_contract_listboard_url',
    'pi_listboard_url': 'cms_dashboard:pi_listboard_url',
    'pi_dashboard_url': 'cms_dashboard:pi_dashboard_url',
    'consultant_contract_listboard_url': 'cms_dashboard:'
                                         'consultant_contract_listboard_url',
    'consultant_listboard_url': 'cms_dashboard:consultant_listboard_url',
    'consultant_dashboard_url': 'cms_dashboard:consultant_dashboard_url',
    'contract_listboard_url': 'cms_dashboard:contract_listboard_url',
}

DASHBOARD_BASE_TEMPLATES = {
    'listboard_base_template': 'cms/base.html',
    'contract_listboard_template': 'cms_dashboard/contract/contract_listboard.html',
    'allcontracts_listboard_template': 'cms_dashboard/contract/'
                                       'allcontracts_listboard.html',
    'dashboard_base_template': 'cms/base.html',
    'employee_dashboard_template': 'cms_dashboard/employee/employee_dashboard.html',
    'employee_listboard_template': 'cms_dashboard/employee/employee_listboard.html',
    'pi_dashboard_template': 'cms_dashboard/pi/pi_dashboard.html',
    'pi_listboard_template': 'cms_dashboard/pi/pi_listboard.html',
    'consultant_listboard_template': 'cms_dashboard/consultant/consultant_listboard.html',
    'consultant_dashboard_template': 'cms_dashboard/consultant/consultant_dashboard.html',
}
