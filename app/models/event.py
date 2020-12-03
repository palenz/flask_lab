class Event():

    def __init__(self, date, name, number_of_guests, recurring, room_location, description):
        self.name = name
        self.date = date
        self.number_of_guests = number_of_guests
        self.recurring = recurring
        self.room_location = room_location
        self.description = description
