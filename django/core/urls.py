from django.urls import path
from .views import index_view, sermons_view

app_name = 'core'

urlpatterns = [
    path('', index_view, name="home"),
    path('sermons/', sermons_view, name="sermons"),
    # path('/')
]
