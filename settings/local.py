from .base import *

# Configuración de la base de datos MySQL.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "OPTIONS": {
            "read_default_file": "C:/Users/jaime/OneDrive/Escritorio/Django-Codigo-facilito/settings/my.cnf",
        },
    }
}
