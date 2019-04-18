"""qwerty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from qwerty import views
from django.shortcuts import render

# def index2(request): return render(request, 'template/x2.html')
def index2(request): return render(request, 'index2.html')
def index3(request): return render(request, 'index3.html')

def index1(request): return render(request, 'index.html')
def parsename(request, name, age, city):
	# result = f'Меня зовут <b>{name}</b>, i\'m <b>{age}</b> olg and i love  <a href="gogole.com/q={age}">{age}</a>'
	return render(request, 'show_name.html',
			context={
				'name' : name,
				'age' : age,
				'city' : city
			})
	# return render(request, 'show_name.html', context={'name': request.GET['name']})

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('indexx2/', views.index2),
    path('', index1),
    path('indexx2/', index2),
    path('indexx3/', index3),
    path('pirate/<str:name>/<int:age>/<str:city>', parsename),
    

]
