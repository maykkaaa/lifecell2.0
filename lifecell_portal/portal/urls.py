from django.urls import path

from . import views


app_name = "portal"


urlpatterns = [
    path(
        "",
        views.ForumTopicListView.as_view(),
        name="forum"
    ),

    path(
        "create/",
        views.ForumTopicCreateView.as_view(),
        name="forum_topic_create"
    ),

    path(
        "<int:pk>/",
        views.ForumTopicDetailView.as_view(),
        name="forum_topic"
    ),

    path(
        "<int:pk>/message/create/",
        views.ForumMessageCreateView.as_view(),
        name="forum_message_create"
    ),

    path(
        "message/<int:pk>/edit/",
        views.ForumMessageUpdateView.as_view(),
        name="forum_message_edit"
    ),

    path(
        "message/<int:pk>/delete/",
        views.ForumMessageDeleteView.as_view(),
        name="forum_message_delete"
    ),

    path(
        "diary/",
        views.GradeListView.as_view(),
        name="diary"
    ),
]