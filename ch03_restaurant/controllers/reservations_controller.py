from flask import render_template, request, redirect, url_for, Blueprint
from services.restaurants_service import RestaurantService
from services.reservations_service import ReservationService
from utils.dto import ReservationFormDto

reservations_blueprint = Blueprint('reservations', __name__)
restaurant_service = RestaurantService()
reservation_service = ReservationService()

@reservations_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        restaurants = restaurant_service.get_restaurants()
        return render_template('index.html', restaurants=restaurants)
    if request.method == 'POST':
        restaurant_id = request.form['restaurant_id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        num_guests = request.form['num_guests']
        date = request.form['date']
        reservation = ReservationFormDto(restaurant_id, name, email, phone, num_guests, date)
        reservation_service.add(reservation)
        return redirect(url_for('reservations.index'))
    
@reservations_blueprint.route('/manage')
def manage():
    reservations = reservation_service.get_reservations()
    return render_template('manage_reservations.html', reservations=reservations)

@reservations_blueprint.route('/cancel_reservation/<id>')
def cancel(id):
    reservation_service.cancel(id)
    return redirect(url_for('reservations.manage'))