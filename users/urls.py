from django.conf.urls import url

from users import views

urlpatterns = [
    url(r'^index$', views.index, name="index"),
    url(r'^news1/(\d+)/(\d+)$', views.news1),
    url(r'^news2/(?P<category>\d+)/(?P<page>\d+)$', views.news2),
    url(r'^news3$', views.news3),
    url(r'^news4$', views.news4),
    url(r'^news5$', views.news5),
    url(r'^news6$', views.news6),
    url(r'^news7$', views.news7),
    url(r'^get_session$', views.get_session),
    url(r'^set_session$', views.set_session),
    url(r'^del_session$', views.del_session),
    url(r'^get_cookie$', views.get_cookie),
    url(r'^set_cookie$', views.set_cookie),
    url(r'^resp$', views.resp),
    url(r'^resp2$', views.resp2),
    url(r'^resp3$', views.resp3),
    url(r'^resp4$', views.resp4),

    url(r'^post$', views.post),
    url(r'^do_post$', views.do_post),
    url(r'^post2', views.PostView.as_view())

]