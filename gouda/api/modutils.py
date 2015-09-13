from gouda.settings import Settings


_settings = Settings("config/settings.json")

BOTNAME = _settings.core['nick']
