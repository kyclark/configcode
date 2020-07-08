#!/usr/bin/env python3

import algorithm

flds = [
    'VERSION', 'ALGORITHM_AUTHOR', 'ALGORITHM_AUTHOR_EMAIL',
    'WRITE_BETYDB_CSV', 'BOGUS'
]

print('Using has/getattr()')
for fld in filter(lambda f: hasattr(algorithm, f), flds):
    val = getattr(algorithm, fld)
    print('{:25} => {} ({})'.format(fld, val, type(val)))

print()
print('Using getattr() with default')
for fld in flds:
    val = getattr(algorithm, fld, 'NA')
    print('{:25} => {} ({})'.format(fld, val, type(val)))

print()
print('Using dir()')
available = list(filter(lambda f: not f.startswith('__'), dir(algorithm)))
for fld in filter(lambda f: f in available, flds):
    val = getattr(algorithm, fld)
    print('{:25} => {} ({})'.format(fld, val, type(val)))
