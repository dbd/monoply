import os

SECURITY_QUESTIONS = {'What was your favorite place to visit as a child?':
                      os.environ.get('SQ1'),
                      'In what town or city was your first full time job?':
                      os.environ.get('SQ2'),
                      "What was your first pet's name?":
                      os.environ.get('SQ3')}

SPREADSHEET_NAME = 'Name of spreadsheet'
WORKSHEET = 'Name of tab on work sheet'
JSON_KEY_FILE = 'key.json'
