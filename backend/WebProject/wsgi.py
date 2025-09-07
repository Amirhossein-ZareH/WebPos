"""
WSGI config for ShopProject project.

این فایل به عنوان entry point برای سرور وب استفاده می‌شود.
"""

import os
from django.core.wsgi import get_wsgi_application

# مسیر تنظیمات پروژه
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebProject.settings')

application = get_wsgi_application()
