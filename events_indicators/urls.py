from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='events_indicators'),
    url(r'^/graphic/(?P<graphic_id>[0-9]+)/$',views.graphic_detail, name='events_graphic_detail'),
]
