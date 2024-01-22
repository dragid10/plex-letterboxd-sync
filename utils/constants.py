from decouple import config

# Plex vars
PLEX_USERNAME = config("PLEX_USERNAME")
PLEX_PASSWORD = config("PLEX_PASSWORD")
PLEX_2FA = config("PLEX_2FA", default=None)

# Letterboxd Vars
LETTERBOXD_USERNAME = config("LETTERBOXD_USERNAME")