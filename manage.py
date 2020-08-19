from flask import Flask


def create_app():
    app_new = Flask(__name__)
    from app.main import self as main_blueprint
    app_new.register_blueprint(main_blueprint)
    return app_new


app = create_app()


if __name__ == '__main__':
    app.run()
