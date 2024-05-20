from flask import Flask
from controllers.reservations_controller import reservations_blueprint

app = Flask(__name__)

app.register_blueprint(reservations_blueprint)

if __name__ == '__main__':
    app.run(debug=True)