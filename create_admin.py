import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vehicleservicemanagement.settings')
django.setup()

from django.contrib.auth.models import User, Group

# Create admin group if it doesn't exist
admin_group, created = Group.objects.get_or_create(name='ADMIN')

# Get the superuser
superuser = User.objects.filter(is_superuser=True).first()

if superuser:
    # Add superuser to admin group
    admin_group.user_set.add(superuser)
    print(f"Added superuser {superuser.username} to ADMIN group")
else:
    print("No superuser found. Please create a superuser first using 'python manage.py createsuperuser'") 