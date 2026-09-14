from django.urls import path

from .views import GradeListView


app_name = "diary"


urlpatterns = [
    path(
        "",
        GradeListView.as_view(),
        name="list"
    ),
]