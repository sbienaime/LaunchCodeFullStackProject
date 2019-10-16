from django.conf.urls import url
from EzdocsApp import views
# SET THE NAMESPACE!
app_name = 'EzdocsApp'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^see_docs/$',views.see_docs,name='see_docs'),
]
