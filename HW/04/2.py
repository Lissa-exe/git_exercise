# Feb 12 2019 2:41PM сделает 2019-02-12 14:41:00

import datetime

some_date = 'Feb 12 2019 2:41PM'

some_date = datetime.datetime.strptime(some_date, '%b %d %Y %I:%M%p').strftime('%Y-%m-%d %H:%M:%S')
print(some_date)





