"""projectname URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from awaazapp.views import article,throttle

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^v1/post-project/',article.postinfo),
    url(r'^v1/posttask/',article.posttask),
    url(r'^v1/view-project/',article.listing),
    url(r'^v1/showtasks/',article.showtasks),
    url(r'^v1/deleteinfo/',article.deleteinfo),

    url(r'^v1/get-members/', throttle.get_all_member),

    url(r'^',article.welcome),
]