import os
import sys

# Django ilovasi uchun to‘g‘ri yo‘lni qo‘shish
sys.path.append('/var/www/hccs/gidro-arxiv')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'arxiv_config.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

