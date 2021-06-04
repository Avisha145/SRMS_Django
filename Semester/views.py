from django.shortcuts import render

# Create your views here.
def semester_mgmt_view(request):
	return render(request, 'semester_mgmt.html', {})

def semester_update_view(request):
	return render(request, 'semester_update.html', {})