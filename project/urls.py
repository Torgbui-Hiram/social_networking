from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import community



urlpatterns = [
    path('', include('timeline.urls')),
    path('', include('posts.urls')),
    path('', include('accounts.urls')),
    path('', include('notification.urls')),
    # path('', include('community.urls')),
    path('', include('search.urls')),
    path('admin/admin', admin.site.urls),


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'posts.views.error_404_view'