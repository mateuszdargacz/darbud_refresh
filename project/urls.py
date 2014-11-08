from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView


admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^ajax/', include('apps.cms_plugins.contact_form.urls', namespace='ajax')),
                       url(r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog'),
                       url(r'^zohoverify/verifyforzoho.html/?$',
                           TemplateView.as_view(template_name='pages/verifyforzoho.html')),
                       url(r'^admin/', include(admin.site.urls)),


) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
    # + static('/pl/', document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns('',
                             url(r'^', include('cms.urls')),
)