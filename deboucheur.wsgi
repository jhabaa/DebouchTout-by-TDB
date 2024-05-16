#!/usr/bin/python
import sys
import logging
import os


logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/deboucheur/")
#config
os.environ['FLASK_APP'] = 'deboucheur'
os.environ['FLASK_ENV'] = 'production'

from deboucheur import app as application
