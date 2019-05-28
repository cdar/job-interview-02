import os
import sys

from django.contrib.auth import get_user_model
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'secureaccesssite.settings.dev')
sys.path.append('secureaccesssite')

django.setup()

User = get_user_model()

for i in range(3):
    name = 'user{}'.format(i)
    User.objects.create_user(name, password=name)

User.objects.create_superuser('admin', 'admin@localhost', 'admin')
