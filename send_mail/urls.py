from django.urls import path
from .views import Email_sender
app_name='test'
urlpatterns=[
    path('em',Email_sender,name='em'),

]