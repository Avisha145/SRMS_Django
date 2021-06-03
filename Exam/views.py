from django.shortcuts import render

# Create your views here.
def exam_mgmt_view(request):
	return render(request, 'exam_mgmt.html', {})