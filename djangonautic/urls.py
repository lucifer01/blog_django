from django.contrib import admin
from django.urls import path, re_path, include
from . import views
#staticfiles_urlpatterns will setup urlpatterns & serves the static files
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# static will setup url patterns about  media-url &  media-directory ,
# and serves the media files
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^articles/',include('articles.urls')),
    re_path(r'^accounts/',include('accounts.urls')),
    re_path(r'^$',article_views.article_list,name='home'),
    re_path(r'^about/$',views.about)

]

#urlpatterns += staticfiles_urlpatterns()
urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
