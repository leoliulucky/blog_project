from django.conf.urls import url
from blog.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    # url(r'^archive/$', archive, name='archive'),
    # url(r'^article/$', article, name='article'),
    # url(r'^article/(?P<id>\d+)$', article),
    url(r'^comment/post/$', comment_post, name='comment_post'),
    url(r'^logout$', do_logout, name='logout'),
    url(r'^reg', do_reg, name='reg'),
    url(r'^login', do_login, name='login'),
    url(r'^category/(?P<cid>\d+)$', category, name='category'),
    url(r'^category/list$', list_category, name='list_category'),
    url(r'^archive/list$', list_archive, name='list_archive'),
    url(r'^about$', about, name='about'),
    url(r'^blog/(?P<id>\d+)$', article, name='article'),
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})$', archive, name='archive'),
    url(r'^tag/(?P<tid>\d+)$', tag, name='tag'),
]
