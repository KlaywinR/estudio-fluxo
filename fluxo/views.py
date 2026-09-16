from django.shortcuts import render


def home(request):
	return render(request, 'fluxo/home.html')


def portfolio(request):
	return render(request, 'fluxo/portfolio.html')
