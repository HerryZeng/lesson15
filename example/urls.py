from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', admin.site.urls),
    path('poems/', views.PoemListView.as_view(), name='poem_list'),
    # path('poem/(?P<pk>[0-9]+)$', view=views.poem_detail, name='poem_detail'),
    url(r'^poem/(?P<pk>[0-9]+)$', view=views.poem_detail, name='poem_detail')
]
