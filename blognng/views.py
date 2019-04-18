from django.http import HttpResponse


def hello(request):
	return HttpResponse('<h1 align="center">Hello! Blognn in view.py from blognn</h1>')