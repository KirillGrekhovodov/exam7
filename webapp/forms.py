from django import forms

from webapp.models import Answer, Choice, Poll


class AnswerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        pk = kwargs.pop("pk")
        super().__init__(*args, **kwargs)
        self.fields["option"].queryset = Choice.objects.filter(poll__pk=pk)

    class Meta:
        model = Answer
        exclude = ["poll"]
        widgets = {"option": forms.RadioSelect()}


class AddUsersForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ["users"]
        widgets = {"users": forms.CheckboxSelectMultiple()}
