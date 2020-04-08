from flask import Flask
from hotline.config import config_env_files


def configure_app(new_app, config_name='development'):
    new_app.config.from_object(config_env_files[config_name])

app = Flask(__name__)
import hotline.views

configure_app(app)
