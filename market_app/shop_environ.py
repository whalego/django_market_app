
API_VERSION = "v1"

# リリース時に変更する必要あり
SECRET_KEY = "secret_key_env"

DATABASES_ENV = {
    "default": {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shop',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '192.168.33.10',
        'PORT': '3306'
    }
}
