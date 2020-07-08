#!/usr/bin/env python3

import config_type

config = config_type.config()
tmpl = '{:25} => {}'
print(tmpl.format('AUTHOR', config.author))
print(tmpl.format('EMAIL', config.author_emails))
print(tmpl.format('VERSION', ','.join(config.write_betydb_csv)))
