from decouple import config

API_HASH = config("API_HASH")
API_TOKEN = config("API_TOKEN", cast=int)
TELEGRAM_STRING_SESSION = config("TELEGRAM_STRING_SESSION")
CHANNEL_ID_AO_VIVO = config("CHANNEL_ID_AO_VIVO", cast=int)
CHANNEL_ID_24H = config("CHANNEL_ID_24H", cast=int)
CHANNEL_ID_METODO_CONSISTENTE = config("CHANNEL_ID_METODO_CONSISTENTE", cast=int)
# TODO: Checar se não fica melhor colocar os canais como variaveis de ambiente
CHANNEL_ID_TO_NAME = {"1217336884": "signals_elite", "1201518926": "bot_sinais_24h", "1378888625": "corujao"}
