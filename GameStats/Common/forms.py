from django import forms
from GameStats.Common.models import Problem, StaffChat


class ReportProblemForm(forms.ModelForm):
    video_image = forms.URLField(widget=forms.URLInput(attrs={
        "placeholder": "Please submit a link to a video and/or image that shows the problem, if you have one."
    }),
        required=False,
        label="URL")

    creator = forms.CharField(disabled=True)

    class Meta:
        model = Problem
        fields = "__all__"


class StaffChatForm(forms.ModelForm):
    content = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Type your message here..."}), label="")
    image = forms.ImageField(required=False)
    creator = forms.CharField(disabled=True)

    class Meta:
        model = StaffChat
        fields = '__all__'

