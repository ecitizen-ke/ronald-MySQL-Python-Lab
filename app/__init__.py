from flask import Flask
from app.views import state_bp

#/home/ron/.local/bin/virtualenvwrapper.sh
def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile("config.py")
    app.register_blueprint(state_bp)
    return app


