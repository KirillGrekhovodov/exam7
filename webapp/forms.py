from django import forms

from webapp.models import Answer, Choice


class AnswerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        pk = kwargs.pop("pk")
        super().__init__(*args, **kwargs)
        self.fields["option"].queryset = Choice.objects.filter(poll__pk=pk)

    class Meta:
        model = Answer
        exclude = ["poll"]
        widgets = {"option": forms.RadioSelect()}
