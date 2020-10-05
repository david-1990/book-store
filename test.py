from datetime import datetime
from travel.user import User
from travel.booking import Booking
from travel.city import City

u = User()
u.register('jill', 'ueio', 'jilly@y.com')

c = City('Brisbane', 'City in Queensland with good weather')

start_date = datetime(2019,11,23)
end_date = datetime(2019,11,30)
b = Booking(start_date, end_date, c, u)

print(b)
print('Access city description of booking:', b._city.description)