
from django.contrib import admin
from django.conf.urls import url
from TEST.views import *


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^loginform/$',home,name="login"),
    url(r'^signupform/$', signup,name="signup"),
    url(r'^sign/$', login, name="login"),
    url(r'^logout/$', logout, name="logout"),

]
