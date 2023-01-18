import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv
from corsheaders.defaults import default_headers

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEVELOPMENT")

ALLOWED_HOSTS = ["ms4-scifi-zone.herokuapp.com", "localhost", "127.0.0.1"]

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "corsheaders",
    "home",
    "tickets",
    "guests",
    "bag",
    "checkout",
    "profiles",
    "find",
    # OTHER
    "crispy_forms",
    "storages",
    "watson",
    "django_extensions",
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
    "csp.middleware.CSPMiddleware",
    "watson.middleware.SearchContextMiddleware",
]

CSP_DEFAULT_SRC = ["'none'"]

CSP_SCRIPT_SRC = [
    "'self'",
    "https://js.stripe.com",
    "https://checkout.stripe.com",
    "https://*.stripe.com",
    "https://*.fontawesome.com",
    "https://ms4-scifi-zone.herokuapp.com/",
    "https://*.jsdelivr.net",
    "https://*.jquery.com",
    "https://ms4-scifi-zone.s3.amazonaws.com/static/js/base.js",
    "https://ms4-scifi-zone.s3.amazonaws.com/static/checkout/js/stripe_elements.js",
    "https://ms4-scifi-zone.herokuapp.com/checkout/cache_checkout_data/",
]

CSP_SCRIPT_SRC_ELEM = [
    "'self'",
    "https://js.stripe.com",
    "https://checkout.stripe.com",
    "https://*.stripe.com",
    "https://*.fontawesome.com",
    "https://ms4-scifi-zone.herokuapp.com/",
    "https://*.jsdelivr.net",
    "https://*.jquery.com",
    "https://ms4-scifi-zone.s3.amazonaws.com/static/js/base.js",
    "https://ms4-scifi-zone.s3.amazonaws.com/static/checkout/js/stripe_elements.js",
    "https://ms4-scifi-zone.herokuapp.com/checkout/cache_checkout_data/",
]

CSP_STYLE_SRC = [
    "'unsafe-inline'",
    "https://cdn.jsdelivr.net",
    "https://ms4-scifi-zone.s3.amazonaws.com/static/css/base.css",
    "http://127.0.0.1:8000/static/css/base.css",  # needed for development
]

CSP_FONT_SRC = [
    "https://ms4-scifi-zone.s3.amazonaws.com/static/fonts/",
    "https://ka-p.fontawesome.com/releases/v6.1.1/webfonts/",
    "http://127.0.0.1:8000/static/fonts/",
]  # needed for development

CSP_FRAME_SRC = [
    "https://js.stripe.com/",
    "https://hooks.stripe.com",
    "https://checkout.stripe.com",
    "https://*.stripe.network",
]

CSP_CONNECT_SRC = [
    "https://ka-p.fontawesome.com/releases/v6.1.1/",
    "https://api.stripe.com",
    "https://checkout.stripe.com",
    "https://*.stripe.com",
    "https://*.jquery.com",
    "https://ms4-scifi-zone.s3.amazonaws.com/static/checkout/js/stripe_elements.js",
    "https://ms4-scifi-zone.herokuapp.com/checkout/cache_checkout_data/",
    "https://ms4-scifi-zone.herokuapp.com/checkout/checkout_success/",
]

CSP_INCLUDE_NONCE_IN = ["script-src"]

CSP_IMG_SRC = [
    "'self'",
    "https://ms4-scifi-zone.s3.amazonaws.com/media/",
    "https://*.stripe.com",
]

CORS_ALLOWED_ORIGINS = [
    "https://herokuapp.com",
    "https://stripe.com",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

CSRF_TRUSTED_ORIGINS = [
    "http://stripe.com",
    "http://r.stripe.com",
    "http://js.stripe.com",
]

CORS_ALLOW_HEADERS = list(default_headers) + [
    "my-custom-header",
]

# settings from "Django for Professionals" by William S. Vincent
# prevent data sniffing
SECURE_SSL_REDIRECT = os.environ.get(
    "DJANGO_SECURE_SSL_REDIRECT", default=True
)

# add Strict-Transport-Security header:
SECURE_HSTS_SECONDS = 300  # change to much greater value later

# force subdomains to use SSL
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# because SECURE_HSTS_SECONDS has non-zero value
SECURE_HSTS_PRELOAD = True

# force cookies over HTTPS
SESSION_COOKIE_SECURE = os.environ.get(
    "DJANGO_SESSION_COOKIE_SECURE", default=True
)

# send only cookies marked as secure with an HTTPS connection
CSRF_COOKIE_SECURE = os.environ.get("DJANGO_CSRF_COOKIE_SECURE", default=True)

CRISPY_TEMPLATE_PACK = "uni_form"

ROOT_URLCONF = "scifi_zone.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
            os.path.join(BASE_DIR, "templates", "allauth"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.media",
                "csp.context_processors.nonce",
                "bag.contexts.bag_contents",
                "csp.context_processors.nonce",
            ],
            "builtins": [
                "crispy_forms.templatetags.crispy_forms_tags",
                "crispy_forms.templatetags.crispy_forms_field",
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 1

ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/"

WSGI_APPLICATION = "scifi_zone.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

if "DATABASE_URL" in os.environ:
    DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL")),
    }

else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

if "USE_AWS" in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        "Expires": "Thu, 31 Dec 2099 20:00:00 GMT",
        "CacheControl": "max-age=94608000",
    }

    # Bucket config
    AWS_STORAGE_BUCKET_NAME = "ms4-scifi-zone"
    AWS_S3_REGION_NAME = "eu-central-1"
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

    # Static and media files
    STATICFILES_STORAGE = "custom_storages.StaticStorage"
    STATICFILES_LOCATION = "static"
    DEFAULT_FILE_STORAGE = "custom_storages.MediaStorage"
    MEDIAFILES_LOCATION = "media"

    # Override static and media URLs in production
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/"
    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Stripe
VAT_PERCENTAGE = 19
STRIPE_PUBLIC_KEY = os.environ.get("STRIPE_PUBLIC_KEY")
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY")
STRIPE_CURRENCY = "eur"
STRIPE_WH_SECRET = os.environ.get("STRIPE_WH_SECRET")

# Mail
if "DEVELOPMENT" in os.environ:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
    DEFAULT_FROM_EMAIL = "scifizone@example.com"
else:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASS")
    DEFAULT_FROM_EMAIL = os.environ.get("EMAIL_HOST_USER")
