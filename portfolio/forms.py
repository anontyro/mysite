from django import forms
from .models import Portfolio
from pagedown.widgets import PagedownWidget
from django.contrib.admin.widgets import AdminDateWidget

class PortfolioForm(forms.ModelForm):
    body = forms.CharField(widget=PagedownWidget)
    code = forms.CharField(widget=PagedownWidget)
    class Meta:
        model = Portfolio
        fields = [
            "title",
            "draft",
            "gitLink",
            "image",
            "body",
            "code",
            "tags"
        ]