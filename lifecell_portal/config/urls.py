from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import LoginView, LogoutView

from core.views import HomeView


urlpatterns = [
    path(
        "",
        HomeView.as_view(),
        name="home"
    ),

    path(
        "admin/",
        admin.site.urls
    ),

    path(
        "forum/",
        include("portal.urls")
    ),

    path(
        "diary/",
        include("portal.diary_urls")
    ),

    path(
        "login/",
        LoginView.as_view(
            template_name="registration/login.html"
        ),
        name="login"
    ),

    path(
        "logout/",
        LogoutView.as_view(
            next_page="home"
        ),
        name="logout"
    ),

    path(
        "accounts/",
        include("accounts.urls")
    ),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )