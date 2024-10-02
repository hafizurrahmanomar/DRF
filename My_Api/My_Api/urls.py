
from django.contrib import admin
from django.urls import path ,include

# for image loading
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apiV1/', include('status.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
