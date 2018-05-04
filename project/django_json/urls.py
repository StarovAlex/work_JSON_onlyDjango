# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import JSONAddView, JSONGetView


urlpatterns = [
    url(regex=r'^$', view=JSONAddView.as_view(), name='add-categories'),
    url(regex=r'(?P<pk>\d+)/$', view=JSONGetView.as_view(), name='get-categories')
]
