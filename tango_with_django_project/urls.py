"""tango_with_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rango import views
#app_name='rango'
urlpatterns = [
    url(r'rango/$', views.index, name='index'),
    url(r'rango/about/', views.about, name='about'),
    #url(r'rango/category/<slug:category_name_slug>/add_page/', views.add_page,name='add_page'),
    url(r'rango/category/<slug:category_name_slug>/', views.show_category,name='show_category'),
    url(r'rango/add_category/', views.add_category, name='add_category'),
    url(r'rango/register/', views.register, name='register'), # New mapping!
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
