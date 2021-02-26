from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls')),

    # to register the service worker at the root of our project
    path('sw.js', TemplateView.as_view(template_name='sw.js', content_type='application/x-javascript')),

    path('webpush/', include('webpush.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)