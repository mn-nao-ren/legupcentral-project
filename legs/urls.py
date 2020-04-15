from django.contrib import admin
from django.urls import path, include
from squads import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
 
    # path('', views.home, name='home'),
 
    path('', views.home, name='home'),
 
    path('accounts/', include('accounts.urls')),
    path('squads/', include('squads.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
