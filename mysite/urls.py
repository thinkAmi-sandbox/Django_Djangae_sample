from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.ImpressionRegisterView.as_view(), name='reg'),
    url(r'^(?P<pk>[0-9]+)/$', views.ImpressionUpdateView.as_view(), name='upd'),
]