from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PortfolioForm
from .models import Portfolio
from django import forms

class Index(generic.ListView):
	template_name = 'portfolio/portfolio.html'
	context_object_name = 'portfolio_list'

	def get_queryset(self):
		return Portfolio.objects.all().order_by("-date")[:25]

class DetailView(generic.DetailView):
	model = Portfolio
	template_name = 'portfolio/detail_view.html'

class PortfolioCreate(LoginRequiredMixin, CreateView):
	login_url = 'personal: login'
	form_class = PortfolioForm
	model = Portfolio

	def get_form(self, form_class=None):
		if form_class is None: form_class = self.get_form_class()
		form = super(PortfolioCreate, self).get_form(form_class)
		# form.fields['body'] = forms.CharField(widget=PagedownWidget)
		return form
