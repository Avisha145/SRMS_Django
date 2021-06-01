from django.shortcuts import render

# Create your views here.
def subject_view(request):
	return render(request, 'subject.html', {})