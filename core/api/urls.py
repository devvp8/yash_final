from django.urls import path,include
from .views import *

urlpatterns = [
    path('querygenerate/',QueryGeneratorView.as_view(),name='query-generate'),
    path('codegenerator/',CodeGeneratorView.as_view(),name='code-generate')
]

