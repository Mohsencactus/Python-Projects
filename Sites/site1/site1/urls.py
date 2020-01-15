from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('home.urls')),
    path('accounts/',include('accounts.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('admin/', admin.site.urls),
]
