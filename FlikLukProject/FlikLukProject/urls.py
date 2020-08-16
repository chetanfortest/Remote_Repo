"""FlikLukProject URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from testapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index_page_view),
    url(r'^home/', views.home_page_view, name = 'home'),
    url(r'^kannada/', views.kannada_page_view),
    url(r'^hindi/', views.hindi_page_view),
    url(r'^telugu/', views.telugu_page_view),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^logout', views.logout_page_view),
    url(r'^signup', views.signup_view),
    url(r'^addmovie', views.addmovie_view),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
