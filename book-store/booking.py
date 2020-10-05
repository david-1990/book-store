from datetime import datetime
from .user import User

class Booking:
    def __init__(self, startdate, enddate, city, user):
        self._startdate=startdate
        self._enddate=enddate
        self._city=city
        self._user=user
        self._num_guests=1

    def __repr__(self):
        str = 'User: {0}Start date: {1},\nEnd date: {2},\nCity: {3},\nNumber of guests: {4}'
        str = str.format(self._user, self._startdate, self._enddate, self._city.name , self._num_guests)
        return str