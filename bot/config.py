from os import environ as env

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", 24986604))
    API_HASH = env.get("TELEGRAM_API_HASH", "afda6f8e5493b9a5bc87656974f3c82e")
    OWNER_ID = int(env.get("OWNER_ID", 7875474866))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "7875474866").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "vdp_v1_bot")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "8000999968:AAEu3iTbU8iHLeWFjs85WQQolbiK3f9J5Zc")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", -1002469590194))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 7))

class Server:
    BASE_URL = env.get("BASE_URL", "ADD YOUR WEB_DNS HERE.....")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
    PORT = int(env.get("PORT", 8080))

    PROXY_TYPE = env.get("PROXY_TYPE")
    PROXY_HOST = env.get("PROXY_HOST")
    PROXY_PORT = env.get("PROXY_PORT")
    PROXY_USERNAME = env.get("PROXY_USERNAME")
    PROXY_PASSWORD = env.get("PROXY_PASSWORD")

    if PROXY_TYPE and PROXY_HOST and PROXY_PORT:
        PROXY = {
            'scheme': PROXY_TYPE,
            'hostname': PROXY_HOST,
            'port': int(PROXY_PORT),
        }

        if PROXY_USERNAME:
            PROXY['username'] = PROXY_USERNAME
        if PROXY_PASSWORD:
            PROXY['password'] = PROXY_PASSWORD
    else:
        PROXY = None

# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'uvicorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'hydrogram': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
