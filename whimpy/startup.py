#!/usr/bin/env python
import os

config = {
 'PORT' : os.environ.get('VCAP_APP_PORT', 80),
 'IP' : os.environ.get('VCAP_APP_HOST', '0.0.0.0') 
}

os.system('python manage.py runserver {IP}:{PORT}'.format(**config)) 
