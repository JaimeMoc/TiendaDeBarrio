from .base import *

# Configuración de la base de datos MySQL.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "OPTIONS": {
            "read_default_file": "/home/suarezjaime/Documentos/TiendaDeBarrio/TiendaDeBarrio/settings/my.cnf",
        },
    }
}
