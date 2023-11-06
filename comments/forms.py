from django import forms
from .models import *
from django.core.exceptions import ValidationError


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']

    def clean_body(self):
        body = self.cleaned_data['body'].lower()
        for w in BadWord.objects.all():
            if str(w) in body:
                raise ValidationError('Комментарий не прошёл автомодерацию')
        return body
