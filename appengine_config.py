from google.appengine.ext import vendor
vendor.add('libs')

import os
on_appengine = os.environ.get('SERVER_SOFTWARE','').startswith('Development')
if on_appengine and os.name == 'nt':
    os.name = None