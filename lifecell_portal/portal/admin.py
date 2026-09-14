from django.contrib import admin
from .models import ForumTopic, ForumMessage

from .models import (
    News,
    Event,
    Announcement,
    Material,
    ForumTopic,
    ForumMessage,
    Grade,
)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "created_at",
    )

    search_fields = (
        "title",
        "content",
    )


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "date",
        "location",
    )

    search_fields = (
        "title",
        "description",
        "location",
    )

    list_filter = (
        "date",
    )


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "created_at",
    )

    search_fields = (
        "title",
        "content",
    )


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "material_type",
        "created_at",
    )

    search_fields = (
        "title",
        "description",
    )

    list_filter = (
        "material_type",
    )

@admin.register(ForumTopic)
class ForumTopicAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "created_at",
    )

    search_fields = (
        "title",
        "content",
        "author__username",
    )

    list_filter = (
        "created_at",
    )


@admin.register(ForumMessage)
class ForumMessageAdmin(admin.ModelAdmin):
    list_display = (
        "topic",
        "author",
        "created_at",
    )

    search_fields = (
        "content",
        "author__username",
        "topic__title",
    )

    list_filter = (
        "created_at",
    )

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "subject",
        "grade",
        "date",
        "work_name",
    )

    search_fields = (
        "student__username",
        "student__first_name",
        "student__last_name",
        "subject",
        "work_name",
    )

    list_filter = (
        "subject",
        "date",
        "grade",
    )

    ordering = (
        "-date",
        "-id",
    )