# This urls.py was not created when app was created
#from django.conf.urls import patterns, url
from django.conf.urls import url
from user_contacts.views import *


# urlpatterns = patterns('',
#       url(r'^$', home),
#       url(r'^all/$', all_contacts),
#       url(r'^add/$', add),
# )

urlpatterns = [
      url(r'^$', ViewTest.home),
      url(r'^all/$', ViewTest.all_contacts),
      url(r'^add/$', ViewTest.add),
      url(r'^create$', ViewTest.create),
]

handler404 = 'mysite.views.my_custom_page_not_found_view'
handler500 = 'mysite.views.my_custom_error_view'
handler403 = 'mysite.views.my_custom_permission_denied_view'
handler400 = 'mysite.views.my_custom_bad_request_view'