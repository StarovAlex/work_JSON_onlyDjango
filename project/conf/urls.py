from __future__ import absolute_import
from django.conf.urls import url, include

# In case of adding new modules
from django_json import urls as django_json_urls

urlpatterns = [
    url('categories/', include(django_json_urls))
]
