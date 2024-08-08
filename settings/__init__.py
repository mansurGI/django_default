import os

ENV_TYPE = os.getenv('ENV_TYPE')

if ENV_TYPE == 'production':
    from .production import *  # noqa 
elif ENV_TYPE == 'staging':
    from .staging import *  # noqa
elif ENV_TYPE == 'ci':
    from .ci import *  # noqa
else:
    try:
        from .local import *  # noqa
    except ImportError:
        from .base import *  # noqa
