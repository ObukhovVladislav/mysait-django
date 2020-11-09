import authapp.views as authapp
from django.urls import path, include

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),

]
