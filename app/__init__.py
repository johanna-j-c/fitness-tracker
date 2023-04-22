from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)

    from .routes import user_bp
    app.register_blueprint(user_bp)

    return app