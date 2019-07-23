
from django.contrib import admin
from django.urls import path, include
import theme.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('theme.urls')),
    path('gallerydetail/', theme.views.gallerydetail, name='gallerydetail'),
    path('lottery/', theme.views.lottery, name='lottery'),
]
