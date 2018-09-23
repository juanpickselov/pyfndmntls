'''This is the EAFP Easier to Ask Forgiveness than Permission '''
p = '/path/to/datafile.dat'

try:
    process_file(f)
except OSError as e:
    print('Could not process file because {}'.format(str(e)))
