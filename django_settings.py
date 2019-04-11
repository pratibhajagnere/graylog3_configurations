import graypy

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(pathname)s:%(lineno)s:%(classname)s()] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django_logs.log',
            'formatter': 'verbose'
        },
        'gelf': {
            'class': 'graypy.GELFUDPHandler',
            'host': 'AWS_INTERNAL_IP',
            'port': 12201,

    'loggers': {
        'django': {
            'handlers':['file'],
            'propagate': True,
            'level':'DEBUG',
        },
        'backend': {
            'handlers': ['file', 'gelf'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}
