from django.shortcuts import render

# Create your views here.
def division_mgmt_view(request):
	return render(request, 'division_mgmt.html', {})