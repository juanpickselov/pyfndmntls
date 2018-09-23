from roots import sqrt
import sys

try:
    print(sqrt(9))
    print(sqrt(2))
    print(sqrt(-9))
    print('This is never printed')
except ValueError as e:
    print(e, file=sys.stderr)
print('Program execution continues normally here.')
