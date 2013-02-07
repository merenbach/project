from django.conf import settings
from django.utils import timezone
import hashlib

def create_token():
	""" Create a random token to use in RSVP urls """
	m = hashlib.md5()
	m.update(settings.SECRET_KEY + str(timezone.now()))
	return m.hexdigest()