from django.shortcuts import render

# Create your views here.
def semester_view(request):
	return render(request, 'semester.html', {})

def semester_update_view(request):
	return render(request, 'semester_update.html', {})