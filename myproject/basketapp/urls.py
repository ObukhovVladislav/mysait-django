import basketapp.views as basketapp
from django.urls import path, include

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.index, name='index'),
    path('add/<int:products_id>', basketapp.add, name='add'),
]
