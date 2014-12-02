import os
import inspect

# Amazon S3 Settings
AWS_KEY = ''
AWS_SECRET_KEY = ''
AWS_BUCKET = 'www.vpr.net'
AWS_DIRECTORY = 'apps/sandbox'

# Frozen Flask
FREEZER_DEFAULT_MIMETYPE = 'text/html'
FREEZER_IGNORE_MIMETYPE_WARNINGS = True

OPEN_CAGE_API_KEY = ''

GOOGLE_MAPS_API_URL = ''
GOOGLE_SPREADSHEET_USER = ''
GOOGLE_SPREADSHEET_PASSWORD = ''
GOOGLE_SPREADSHEET_SOURCE = ''

# Cache Settings (units in seconds)
STATIC_EXPIRES = 60 * 24 * 3600
HTML_EXPIRES = 3600

# Upload Settings (ignores anything included below)
IGNORE_DIRECTORIES = ['.git', 'venv', 'sass', 'templates', 'gimp']
IGNORE_FILES = ['.DS_Store']
IGNORE_FILE_TYPES = ['.gz', '.pyc', '.py', '.rb', '.md']

if AWS_DIRECTORY:
    BASE_URL = 'http://' + AWS_BUCKET + '/' + AWS_DIRECTORY
    FREEZER_BASE_URL = BASE_URL
else:
    BASE_URL = 'http://' + AWS_BUCKET

ABSOLUTE_PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/'
