"""classmates URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from index import views as index_views
from django.conf.urls.static import static 
from django.conf import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$',index_views.index,name='index'),
	url(r'^profile/([0-9]+)/',index_views.profile,name='profile'),
	url(r'^regist',index_views.regist,name='regist'),
	url(r'^logout',index_views.logout,name='logout'),
	url(r'^createclass',index_views.createclass,name='createclass'),
	url(r'^classprofile',index_views.classprofile,name='classprofile'),
	url(r'^about',index_views.about,name='about'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
