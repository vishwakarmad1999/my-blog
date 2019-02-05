from django import template
from urllib.parse import quote_plus

register = template.Library()

def get_dir(value):
	l = []
	for i in dir(value):
		if not i.startswith('_'):
			l.append(i)
	return l


def get_qs(value):
	return quote_plus(value)


register.filter('get_dir', get_dir)
register.filter('get_qs', get_qs)