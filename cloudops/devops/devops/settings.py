# -*- coding: utf-8 -*-
"""
Django settings for devops project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
import datetime
import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+2xom0^1uq+#y(djh*bp%nlg5e1g#1f)x-^(f%&ojeuyf$2qlu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'workflow',
    'database',
    'CMDB',
    'opscenter',
    'cloud',
    'usercenter',
    # 'channels',
    'worksheet',
    'django_celery_beat',
	'cijenkins',
    'rest_framework',
    'django_filters',
    'guardian',
    'costcenter'
]

""" WebSocket """
# ASGI_APPLICATION = "opscenter.routing.application"
#
# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels_redis.core.RedisChannelLayer",
#         "CONFIG": {
#             "hosts": [("localhost", 6379)],
#         },
#     },
# }
""" WebSocket """

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'opscenter.disable_csrf.DisableCSRFCheck',
]

ROOT_URLCONF = 'devops.urls'

# AUTH_USER_MODEL = 'usercenter.User'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'usercenter.authentication.EmailAuthBackend',
    'guardian.backends.ObjectPermissionBackend',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'devops.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aukey_codeops',
        'USER': 'aukey_codeops',
        'PASSWORD': 'IT@opsDev123',
        'HOST': '10.1.1.86',
        'PORT': 3306,
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
LOGIN_URL = '/login/'

# session 设置
SESSION_COOKIE_AGE = 60 * 60    # 60分钟
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True    # False：会话cookie可以在用户浏览器中保持有效期。True：关闭浏览器，则Cookie失效。

# 定义上传的目录
# MEDIA_ROOT = os.path.join(BASE_DIR, 'static/upload')
MEDIA_ROOT = '/data/uploads'

"""用户模块扩展部分"""
AUTH_PROFILE_MODULE = 'djangoadmin.usercenter.UserProfile'
"""用户模块扩展完成"""

"""邮箱发送模块部分"""
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = u'smtp.exmail.qq.com'                       # SMTP地址 例如: smtp.exmail.qq.com
EMAIL_PORT = 25                     # SMTP端口 例如: 25
EMAIL_HOST_USER = u'devops@aukeys.com'                 # 邮箱例如: xxxxxx@aukeys.com
EMAIL_HOST_PASSWORD = u'Ops@aukey#!123'             # 我的邮箱密码例如: xxxxxxxxx
EMAIL_SUBJECT_PREFIX = u'[傲基运维]'       # 为邮件Subject-line前缀,默认是'[django]'
EMAIL_FROM = u'傲基运维 <devops@aukeys.com>'
EMAIL_USE_TLS = False                  # 与SMTP服务器通信时，是否启动TLS链接(安全链接)。默认是false
EMAIL_USE_SSL = False
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
"""邮箱发送模块完成"""

DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880
'''设置最大POST/GET参数数量'''
DATA_UPLOAD_MAX_NUMBER_FIELDS = 5242880
'''设置最大POST/GET参数数量完成'''

""" inception configure """
INCEPTION_HOST = '10.1.1.86'
INCEPTION_PORT = 6669
INCEPTION_USER = 'aukey_inc'
INCEPTION_PASSWORD = 'Aukey@inc2018'
""" inception configure """

""" celery 配置 """
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
CELERY_TASK_SERIALIZER = 'pickle'
CELERY_ACCEPT_CONTENT = ['json', 'pickle']
CELERY_RESULT_SERIALIZER = 'json'
""" celery 配置 """

""" 周期性任务定义 """
# CELERYBEAT_SCHEDULER = 'django_celery_beat.schedulers.DatabaseScheduler'
""" 周期性任务定义 """

""" 信息中心 """
DOMAIN = 'http://codeops.aukeyit.com'
EMAIL_API = 'http://10.1.1.192:8011/api/v1/msg/email/'
WECHAT_API = 'http://10.1.1.192:8011/api/v1/msg/wechat/'
""" 信息中心 """

""" 脚本执行API """
SCRIPT_API = 'http://10.1.1.192:8111/ans/'
""" 脚本执行API """

""" Ansible执行模块 """
MODULE_API = 'http://10.1.1.192:8111/module/'
""" Ansible执行模块 """

""" 脚本文本生成文件 """
FILE_API = 'http://10.1.1.192:8111/file/'
""" 脚本文本生成文件 """

""" 监控信息RedisAPI """
MONITOR_REDIS_API = '10.1.1.192:8113'
""" 监控信息RedisAPI """

""" 处理pymysql模块 """
from pymysql import install_as_MySQLdb
install_as_MySQLdb()

def mysqldb_escape(value, conv_dict):
    from pymysql.converters import encoders
    vtype = type(value)
    encoder = encoders.get(vtype)
    return encoder(value)

import pymysql
setattr(pymysql, 'escape', mysqldb_escape)
del pymysql
""" 处理pymysql模块 """

"""framework"""
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.DjangoModelPermissions',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
    ),
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'PAGE_SIZE': 100
}
"""framework"""
MONGO_URL = '10.1.1.192'
MONGO_PORT = 27017

ASGI_APPLICATION = "opscenter.routing.application"

# 有效期限
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=4),
    'JWT_AUTH_HEADER_PREFIX': 'OPS',   # JWT跟前端保持一致，比如“token”这里设置成OPS
}

# 解决跨域请求
CORS_ORIGIN_ALLOW_ALL = True