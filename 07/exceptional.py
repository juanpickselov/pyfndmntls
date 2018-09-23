import sys

'''A Module for demonstrating exceptions.'''


def convert(s):
    '''Convert to an integer.'''
    '''Doing this in  the REPL the order of the messages is OK
        but running from a test module the messages and results don't show
        in decent order
    '''
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print('Conversion error: {}'.format(str(e)), file=sys.stderr)
        return -1
    return x


def string_log(s):
    v = convert(s)
    return log(v)
