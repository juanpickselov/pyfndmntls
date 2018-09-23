from roots import sqrt

try:
    print(sqrt(9))
    print(sqrt(2))
    print(sqrt(-1))
    print('This is never printed')
except:
    print('Cannot compute square root of a negative number.')

print('Program execution continues normally here.')
