from django.contrib import admin
from django.urls import path
from core.admin_sites import editor_admin, publisher_admin, archive_admin

urlpatterns = [
    path('admin/', admin.site.urls),  # стандартная админка
    path('editor/', editor_admin.urls),
    path('publisher/', publisher_admin.urls),
    path('archive/', archive_admin.urls),
]