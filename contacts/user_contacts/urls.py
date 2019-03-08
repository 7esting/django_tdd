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
