from django import template
register = template.Library()

def get_dir(value):
	l = []
	for i in dir(value):
		if not i.startswith('_'):
			l.append(i)
	return l

register.filter('get_dir', get_dir)