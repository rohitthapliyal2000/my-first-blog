# Template initialization

from django.core import management
management.call_command('syncdb', interactive=False)
