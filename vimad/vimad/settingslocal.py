# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3-vh_a$2x!^8qr71wk(^l4z689l$hl*^vwq4d@2os+aljx0^ws'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'VIMAD2',
        'USER': 'uservimad',
        'PASSWORD': 'uservimad1234',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
