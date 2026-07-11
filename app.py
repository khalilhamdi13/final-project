from flask import Flask

from service.routes import create_routes


def create_app():
    app = Flask(__name__)
    create_routes(app)
    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
