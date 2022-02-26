from flask import Flask

def create_app(config):
    # app name = RUD
    app = Flask(__name__)

    from rudplus.views.main_views import main_bp
    app.register_blueprint(main_bp)
    return app


if __name__ == "__main__":
    app.run(debug=True)
