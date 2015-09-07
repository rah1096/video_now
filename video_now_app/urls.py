from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    #url(r'^about/$', TemplateView.as_view(template_name='base.html'), name='home'),
    #url(r'^pricing/$', TemplateView.as_view(template_name='base.html'), name='home'),
    #url(r'^contact_us/$', TemplateView.as_view(template_name='pricing.html'), name='home'),
    url(r'^$', 'video_now_app.views.home', name='home'),
    url(r'^staff/$', 'video_now_app.views.staff_home', name='staff'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^videos/$', 'videos.views.category_list', name='video_list'),
    url(r'^videos/(?P<cat_slug>[\w-]+)/$', 'videos.views.category_detail', name='category_detail'),
    url(r'^videos/(?P<cat_slug>[\w-]+)/(?P<id>\d+)/$', 'videos.views.video_detail', name='video_detail'),
    url(r'^admin/', include(admin.site.urls)),
)

#auth login/logout
urlpatterns += patterns('video_now_app.views',
    url(r'^login/$', 'auth_login', name='login'),
    url(r'^logout/$', 'auth_logout', name='logout'),
)