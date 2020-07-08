#!/usr/bin/env python3

import algorithm

config = algorithm.config()
tmpl = '{:25} => {}'
print(tmpl.format('VERSION', config.version))
print(tmpl.format('AUTHOR', config.author))
print(tmpl.format('AUTHOR_EMAIL', config.author_email))
print(tmpl.format('WRITE_BETYDB_CSV', config.write_betydb_csv))
