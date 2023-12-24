from django.urls import path
from myapp.views import index, indexItems

app_name = 'myapp'

urlpatterns = [
    path('', index),
    path('index/<int:my_id>/', indexItems, name='detail')
]
