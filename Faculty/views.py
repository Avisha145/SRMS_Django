from django.shortcuts import render

# Create your views here.

def faculty_view(request):
	return render(request, 'faculty_panel.html', {})

def faculty_mgmt_view(request):
	return render(request, 'faculty_mgmt.html', {})