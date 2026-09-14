from django import forms

from .models import ForumTopic, ForumMessage


class ForumTopicForm(forms.ModelForm):
    class Meta:
        model = ForumTopic
        fields = ("title", "content")
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Назва теми"
            }),
            "content": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 6,
                "placeholder": "Текст першого повідомлення"
            }),
        }

    def clean_title(self):
        title = self.cleaned_data["title"].strip()

        if len(title) < 5:
            raise forms.ValidationError(
                "Назва теми повинна містити щонайменше 5 символів."
            )

        return title

    def clean_content(self):
        content = self.cleaned_data["content"].strip()

        if len(content) < 10:
            raise forms.ValidationError(
                "Повідомлення повинно містити щонайменше 10 символів."
            )

        return content


class ForumMessageForm(forms.ModelForm):
    class Meta:
        model = ForumMessage
        fields = ("content",)
        widgets = {
            "content": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Напишіть повідомлення..."
            }),
        }

    def clean_content(self):
        content = self.cleaned_data["content"].strip()

        if len(content) < 2:
            raise forms.ValidationError(
                "Повідомлення занадто коротке."
            )

        return content