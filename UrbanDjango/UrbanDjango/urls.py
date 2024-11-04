"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from task1.views import (main_page, page_2, bin_page, page_3, button, sign_up_by_html, sign_up_by_django,
                         games, menu_page, go_reg)
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', menu_page, name='menu_page'),
    path('', main_page),
    path('bin/', bin_page),
    path('game/', games, name='games'),
    path('page2/', page_2),
    path('page3/', page_3),
    path('button', button, name='button'),
    path('django_sign_up/', sign_up_by_django, name='django_sign_up'),
    path('registration/', sign_up_by_html, name='registration'),
    path('go_reg/', go_reg, name='go_reg'),
]