from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class News(models.Model):
    title = models.CharField(
        "Заголовок",
        max_length=200
    )

    short_description = models.TextField(
        "Короткий опис"
    )

    content = models.TextField(
        "Повний текст"
    )

    created_at = models.DateTimeField(
        "Дата публікації",
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Новина"
        verbose_name_plural = "Новини"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(
        "Назва події",
        max_length=200
    )

    description = models.TextField(
        "Опис"
    )

    date = models.DateTimeField(
        "Дата та час"
    )

    location = models.CharField(
        "Місце проведення",
        max_length=200,
        blank=True
    )

    created_at = models.DateTimeField(
        "Дата створення",
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Подія"
        verbose_name_plural = "Події"
        ordering = ["date"]

    def __str__(self):
        return self.title


class Announcement(models.Model):
    title = models.CharField(
        "Заголовок",
        max_length=200
    )

    content = models.TextField(
        "Текст"
    )

    created_at = models.DateTimeField(
        "Дата публікації",
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Оголошення"
        verbose_name_plural = "Оголошення"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Material(models.Model):
    MATERIAL_TYPES = [
        ("file", "Файл"),
        ("link", "Посилання"),
        ("youtube", "YouTube"),
    ]

    title = models.CharField(
        "Назва",
        max_length=200
    )

    description = models.TextField(
        "Опис",
        blank=True
    )

    material_type = models.CharField(
        "Тип матеріалу",
        max_length=20,
        choices=MATERIAL_TYPES
    )

    url = models.URLField(
        "Посилання",
        blank=True
    )

    file = models.FileField(
        "Файл",
        upload_to="materials/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        "Дата додавання",
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Матеріал"
        verbose_name_plural = "Матеріали"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class ForumTopic(models.Model):
    title = models.CharField(
        "Назва теми",
        max_length=200
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="forum_topics"
    )
    content = models.TextField(
        "Перше повідомлення"
    )

    created_at = models.DateTimeField(
        "Дата створення",
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Тема форуму"
        verbose_name_plural = "Теми форуму"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

class ForumMessage(models.Model):
    topic = models.ForeignKey(
        ForumTopic,
        on_delete=models.CASCADE,
        related_name="messages"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="forum_messages"
    )
    content = models.TextField(
        "Текст повідомлення"
    )
    created_at = models.DateTimeField(
        "Дата створення",
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Повідомлення форуму"
        verbose_name_plural = "Повідомлення форуму"
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.author.username}: {self.content[:50]}"

class Grade(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="grades",
        verbose_name="Учень"
    )

    subject = models.CharField(
        "Предмет",
        max_length=100
    )

    grade = models.PositiveSmallIntegerField(
        "Оцінка",
        validators=[
            MinValueValidator(1),
            MaxValueValidator(12),
        ]
    )

    date = models.DateField(
        "Дата отримання"
    )

    work_name = models.CharField(
        "Назва роботи",
        max_length=200
    )

    comment = models.TextField(
        "Коментар викладача",
        blank=True
    )

    class Meta:
        verbose_name = "Оцінка"
        verbose_name_plural = "Оцінки"
        ordering = ["-date", "-id"]

    def __str__(self):
        return f"{self.student.username} — {self.subject} — {self.grade}"