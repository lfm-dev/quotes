import os

SETTINGS_FILE_PATH = os.path.join(os.getenv('HOME'), '.config/quotes/settings.csv')

def get_settings():
    settings = {}
    with open(SETTINGS_FILE_PATH, encoding='utf-8') as settings_file:
        for line in settings_file:
            line = line.strip().split(',')
            settings[line[0]] = line[1]
    return settings

SETTINGS = get_settings()
