import basketapp.views as basketapp
from django.urls import path, include

app_name = 'basketapp'

urlpatterns = [
    path('index/', basketapp.index, name='index'),
]
