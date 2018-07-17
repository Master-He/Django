from django.conf.urls import url

from users import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^news1/(\d+)/(\d+)$', views.news1),
    url(r'^news2/(?P<category>\d+)/(?P<page>\d+)$', views.news2),
    url(r'^news3$', views.news3),
    url(r'^news4$', views.news4),
    url(r'^news5$', views.news5),
    url(r'^news6$', views.news6),
    url(r'^news7$', views.news7),
]