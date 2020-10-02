from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("userpage/", include("userpage.urls")),
    path("signup/", include("signup.urls")),
]
