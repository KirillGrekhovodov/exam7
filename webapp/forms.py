from django import forms

from webapp.models import Answer, Choice


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        exclude = ["poll"]
        widgets = {"option": forms.widgets.RadioSelect()}
