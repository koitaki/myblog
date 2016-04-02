from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>\d+)/$', views.post_page, name='post_page'),
    url(r'^add_comment/(\d+)/$', views.add_comment, name='add_comment'),
    url(r'^dummy/$', views.dummy_page, name='dummy_page'),
]
