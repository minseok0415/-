from flask import Flask
from controllers.enroll_controller import enroll_blueprint

app = Flask(__name__)

app.register_blueprint(enroll_blueprint)

if __name__ == '__main__':
    app.run(debug=True)