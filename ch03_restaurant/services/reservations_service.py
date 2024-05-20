from models.reservation import Reservation

class ReservationService:
    def __init__(self):
        self.reservation_db = Reservation()
        
    def get_reservations(self):
        return self.reservation_db.get()
        
    def add(self, dto):
        self.reservation_db.add(dto)
        
    def cancel(self, id):
        self.reservation_db.delete(id)