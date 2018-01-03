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

	paginate_by = 10

	def get_queryset(self):
		query = self.request.GET.get('q')
		if query:
			return Portfolio.objects.active().filter(
				Q(title_icontains = query) |
				Q(body_icontains = query)
				).distinct()
				
		if self.request.user.is_active or self.request.user.is_superuser:
			return Portfolio.objects.all().order_by("-publish")[:25]
		else:
			return list(Portfolio.objects.active().order_by('-publish'))

		

class DetailView(generic.DetailView):
	model = Portfolio
	template_name = 'portfolio/detail_view.html'

class PortfolioCreate(LoginRequiredMixin, CreateView):
	login_url = 'personal:login'
	form_class = PortfolioForm
	model = Portfolio

	def get_form(self, form_class=None):
		if form_class is None: form_class = self.get_form_class()
		form = super(PortfolioCreate, self).get_form(form_class)
		# form.fields['body'] = forms.CharField(widget=PagedownWidget)
		return form

class PortfolioUpdate(LoginRequiredMixin, UpdateView):
	login_url = 'personal:login'
	form_class = PortfolioForm
	model = Portfolio

	def get_form(self, form_class=None):
		form = super(PortfolioUpdate, self).get_form(form_class)
		return form

class PortfolioDelete(LoginRequiredMixin, DeleteView):
	login_url = 'personal:login'
	model = Portfolio
	success_url = reverse_lazy('portfolio:portfolios')
