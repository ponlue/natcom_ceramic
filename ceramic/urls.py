from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path("", include("home.urls")),
<<<<<<< HEAD
    # path('ckeditor', include('ckeditor.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')),
] 
=======
    path('captcha/', include('captcha.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 3957ef5c1cc96c05061adacb9b009e3e7e7ff47d
