from flask import jsonify


def create_routes(app):
    @app.route("/")
    def home():
        return jsonify(
            message="Hello from IBM CI/CD Final Project"
        )

    @app.route("/health")
    def health():
        return jsonify(
            status="OK"
        )
