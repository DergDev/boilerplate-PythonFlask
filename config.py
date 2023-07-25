"""[General Configuration Params]
"""
import os
from os import path
from dotenv import load_dotenv

BASEDIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASEDIR, '.env'))
DEFAULT_VALUE_TO_USE = os.getenv('DEFAULT_VALUE_TO_USE', 'test_default_if_no_dot_env_confs')
API_KEY = os.getenv('API_KEY', 'api_key')
