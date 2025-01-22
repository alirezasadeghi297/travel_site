from django import forms
from blog.models import Comments


class CommnetsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields=['post','name','email','subject','message']