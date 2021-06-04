"""SRMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Login.views import login_view
from Registration.views import registration_view,import_user_view,homepage_view,add_user_view
from Admin.views import admin_view,about_us_view
from Director.views import director_view
from Faculty.views import faculty_view,faculty_mgmt_view
from Student.views import student_view
from Results.views import import_result_view,report_view,student_result_view,manual_result_view 
from Course.views import course_mgmt_view
from Semester.views import semester_mgmt_view,semester_update_view
from Division.views import division_mgmt_view
from Subject.views import subject_mgmt_view
from Exam.views import exam_mgmt_view
from Profile.views import update_user_profile_view,update_student_profile_view



urlpatterns = [
    path('',login_view, name=''),
    path('admin/', admin_view, name='admin'),
    path('login/',login_view, name='login'),
    path('registration/',registration_view, name='registration'),
    path('base/',admin_view, name='base'),
    path('director/', director_view, name='director'),
    path('faculty/', faculty_view, name='faculty'),
    path('student/', student_view, name='student'),
    path('import_user/', import_user_view, name='import_user'),
    path('home/', homepage_view, name='home'),
    path('import_result/', import_result_view, name='import_result'),
    path('course_mgmt/', course_mgmt_view, name='course_mgmt'),
    path('report/', report_view, name='report'),
    path('student_result/', student_result_view, name='student_result'),
    path('semester_mgmt/', semester_mgmt_view, name='semester_mgmt'),
    path('division_mgmt/', division_mgmt_view, name='division_mgmt'),
    path('subject_mgmt/', subject_mgmt_view, name='subject_mgmt'),
    path('faculty_mgmt/', faculty_mgmt_view, name='faculty_mgmt'),
    path('semester_update/', semester_update_view, name='semester_update'),
    path('exam_mgmt/', exam_mgmt_view, name='exam_mgmt'),
    path('manual_result/', manual_result_view, name='manual_result'),
    path('update_user_profile/', update_user_profile_view, name='update_user_profile'),
    path('update_student_profile/', update_student_profile_view, name='update_student_profile'),
    path('add_user/', add_user_view, name='add_user'),
    path('about_us/', about_us_view, name='about_us'),

]
