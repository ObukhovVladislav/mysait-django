"""myproject URL Configuration

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
import myapp.views as myapp
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('', myapp.index, name='index'),

    path('catalog/', myapp.catalog, name='catalog'),

    path('catalog/category/<int:pk>/', myapp.catalog_page, name='catalog_page'),

    path('basket/', myapp.basket, name='basket'),

    path('admin/', admin.site.urls),
]