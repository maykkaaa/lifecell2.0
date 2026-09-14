from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import ForumTopic, ForumMessage, Grade
from .forms import ForumTopicForm, ForumMessageForm


class ForumTopicListView(ListView):
    model = ForumTopic
    template_name = "portal/forum/topic_list.html"
    context_object_name = "topics"


class ForumTopicDetailView(DetailView):
    model = ForumTopic
    template_name = "portal/forum/topic_detail.html"
    context_object_name = "topic"


class ForumTopicCreateView(LoginRequiredMixin, CreateView):
    model = ForumTopic
    form_class = ForumTopicForm
    template_name = "portal/forum/topic_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user

        messages.success(
            self.request,
            "Тему успішно створено!"
        )

        return super().form_valid(form)

    def get_success_url(self):
        return f"/forum/{self.object.pk}/"


class ForumMessageCreateView(LoginRequiredMixin, CreateView):
    model = ForumMessage
    form_class = ForumMessageForm
    template_name = "portal/forum/message_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.topic = ForumTopic.objects.get(
            pk=self.kwargs["pk"]
        )

        messages.success(
            self.request,
            "Повідомлення додано!"
        )

        return super().form_valid(form)

    def get_success_url(self):
        return f"/forum/{self.object.topic.pk}/"


class ForumMessageUpdateView(LoginRequiredMixin, UpdateView):
    model = ForumMessage
    form_class = ForumMessageForm
    template_name = "portal/forum/message_form.html"

    def dispatch(self, request, *args, **kwargs):
        message = self.get_object()

        if (
            message.author != request.user
            and not request.user.is_staff
        ):
            messages.error(
                request,
                "У вас немає прав для редагування цього повідомлення."
            )

            return redirect(
                "portal:forum_topic",
                pk=message.topic.pk
            )

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return f"/forum/{self.object.topic.pk}/"


class ForumMessageDeleteView(LoginRequiredMixin, DeleteView):
    model = ForumMessage
    template_name = "portal/forum/forummessage_confirm_delete.html"

    def dispatch(self, request, *args, **kwargs):
        message = self.get_object()

        if (
            message.author != request.user
            and not request.user.is_staff
        ):
            messages.error(
                request,
                "У вас немає прав для видалення цього повідомлення."
            )

            return redirect(
                "portal:forum_topic",
                pk=message.topic.pk
            )

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return f"/forum/{self.object.topic.pk}/"


class GradeListView(LoginRequiredMixin, ListView):
    model = Grade
    template_name = "portal/diary/grade_list.html"
    context_object_name = "grades"

    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = Grade.objects.select_related(
                "student"
            )
        else:
            queryset = Grade.objects.filter(
                student=self.request.user
            ).select_related("student")

        subject = self.request.GET.get("subject")

        if subject:
            queryset = queryset.filter(
                subject=subject
            )

        date_from = self.request.GET.get("date_from")

        if date_from:
            queryset = queryset.filter(
                date__gte=date_from
            )

        date_to = self.request.GET.get("date_to")

        if date_to:
            queryset = queryset.filter(
                date__lte=date_to
            )

        sort = self.request.GET.get("sort", "-date")

        allowed_sorting = {
            "date": "date",
            "-date": "-date",
            "subject": "subject",
            "-subject": "-subject",
            "grade": "grade",
            "-grade": "-grade",
        }

        sort_field = allowed_sorting.get(
            sort,
            "-date"
        )

        queryset = queryset.order_by(
            sort_field,
            "-id"
        )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_staff:
            students = Grade.objects.values(
                "student__id",
                "student__username",
                "student__first_name",
                "student__last_name",
            ).distinct()

            context["students"] = students
        else:
            context["students"] = None

        subjects = Grade.objects.values_list(
            "subject",
            flat=True
        ).distinct().order_by("subject")

        context["subjects"] = subjects

        context["selected_subject"] = self.request.GET.get(
            "subject",
            ""
        )

        context["selected_date_from"] = self.request.GET.get(
            "date_from",
            ""
        )

        context["selected_date_to"] = self.request.GET.get(
            "date_to",
            ""
        )

        context["selected_sort"] = self.request.GET.get(
            "sort",
            "-date"
        )

        if self.request.user.is_staff:
            context["diary_student"] = "Усі учні"
        else:
            full_name = self.request.user.get_full_name()

            context["diary_student"] = (
                full_name
                if full_name
                else self.request.user.username
            )

        return context