from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^wbsite/', include('wbsite.urls')),

	# user auth urls
	url(r'accounts/login/$', 'proj_iitB.views.login'),
	url(r'accounts/auth/$', 'proj_iitB.views.auth_view'),
	url(r'accounts/logout/$', 'proj_iitB.views.logout'),
	url(r'accounts/loggedin/$', 'proj_iitB.views.loggedin'),
	url(r'accounts/invalid/$', 'proj_iitB.views.invalid_login'),

	# user account register
	url(r'^accounts/register/$', 'proj_iitB.views.register_user'),
	url(r'^accounts/register_success/$', 'proj_iitB.views.register_success'),
]
