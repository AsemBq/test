from django.urls import path

from myapp.views import bib

urlpatterns=[
    path('',bib.as_view())
]