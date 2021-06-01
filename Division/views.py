from django.shortcuts import render

# Create your views here.
def division_view(request):
	return render(request, 'division.html', {})