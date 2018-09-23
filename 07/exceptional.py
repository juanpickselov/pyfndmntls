'''A Module for demonstrating exceptions.'''


def convert(s):
    '''Convert to an integer.'''
    x = -1
    try:
        x = int(s)
        print('Conversion succeeded x =', x)
    except (ValueError, TypeError):
        err_message()
    return x

def err_message():
    print('conversion failure')