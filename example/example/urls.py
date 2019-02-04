from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', auth_views.LoginView.as_view(), {
        'template_name': 'admin/login.html'
    }),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'', include('news.urls')),
    url(r'^$', RedirectView.as_view(
        url=reverse_lazy('news_list', kwargs={'page': 1})
    )),
]
