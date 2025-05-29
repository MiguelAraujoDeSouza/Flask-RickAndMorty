from flask import Flask

# app/__init__.py
def create_app():
    app = Flask(__name__)

    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app