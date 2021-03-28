from flask import Flask, render_template, request
from flask_app.routes.main_route import bp as main_bp
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_app.models import models
from flask_app.routes import routes

# app = Flask(__name__)
# app.register_blueprint(main_bp)
db = SQLAlchemy()
migrate = Migrate(app,db)

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:flaskdb@localhost:5432/Telco'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db) 

    from flask_project.routes import user_route
     app.register_blueprint(user_route.mainbp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)