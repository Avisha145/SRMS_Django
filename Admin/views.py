from django.shortcuts import render

# Create your views here.

def admin_view(request):
	return render(request, 'admin_panel.html', {})

def about_us_view(request):
	return render(request, 'about_us.html', {})
