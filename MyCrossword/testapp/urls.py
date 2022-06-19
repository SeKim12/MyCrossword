from django.urls import re_path
from . import views

urlpatterns = [
    re_path(
        r'^api/testapp/press_button/(?P<pk>[0-9]+)$',
        views.press_button),
    re_path(
        r'^api/testapp/get_frequency/(?P<pk>[0-9]+)$',
        views.get_frequency),
]
