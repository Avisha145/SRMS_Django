from django.shortcuts import render

# Create your views here.
def subject_mgmt_view(request):
	return render(request, 'subject_mgmt.html', {})