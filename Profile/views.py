from django.shortcuts import render

# Create your views here.

def update_user_profile_view(request) : 
	return render(request, 'update_profile.html', {}) 

def update_student_profile_view(request) : 
	return render(request, 'update_student_profile.html', {}) 