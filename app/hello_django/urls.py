from bookstore.views import get_books
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from upload.views import image_upload

urlpatterns = [
    path("", image_upload, name="upload"),
    path("books", get_books),
    path("admin/", admin.site.urls),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
