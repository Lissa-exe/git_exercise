import random

try:
    raise random.choice([ZeroDivisionError, ImportError, KeyError, UnicodeError])
except ZeroDivisionError:
    print('0')
except ImportError:
    print('1')
except KeyError:
    print('2')
except UnicodeError:
    print('3')
