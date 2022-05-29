from django.conf.urls import re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    re_path(r'^$',views.welcome,name = 'welcome'),
    re_path(r'^categories$',views.categories,name = 'categories'),
    re_path(r'^category$', views.category, name='category_results'),
    re_path(r'^location/(\d+)',views.location,name = 'location'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    