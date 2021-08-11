from flask import Flask
from app import api_bp

app = Flask(__name__)
app.register_blueprint(api_bp, url_prefix='/api')
'''
#def create_app(config_filename):
#def create_app():

    app = Flask(__name__)
    #app.config.from_object(config_filename)

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    init_app(app)
    #from Model import db
    #db.init_app(app)

    return app'''



if __name__ == "__main__":
    #app = create_app()
    app.run(debug=True)
