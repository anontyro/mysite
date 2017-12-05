from django import forms
from .models import Portfolio
from pagedown.widgets import PagedownWidget

class PortfolioForm(forms.ModelForm):
    body = forms.CharField(widget=PagedownWidget)
    class Meta:
        model = Portfolio
        fields = [
            "title",
            "body",
            "code",
            "tags",
            "gitLink",
            "image"
        ]