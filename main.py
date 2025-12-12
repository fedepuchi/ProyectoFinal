from flask import Flask
from config import Config
from database import init_db
from routes import workshops_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_db(app)

   
    app.register_blueprint(workshops_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
