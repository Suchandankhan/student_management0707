from django.contrib import admin
from django.urls import path
from stutent_app import views
urlpatterns=[
    path('',views.index,name='index'),
    path('create_course/',views.create_course,name='create_course'),
    path('retrive_course/<int:id>',views.retrive_course,name='retrive_course'),
    path('update_course/<int:id>',views.update_course,name='update_course'),
    path('delete_course/<int:id>',views.delete_course,name='delete_course'),
    path('create_student/<int:id>', views.create_student,name="create_student"),
    path('retrive_student/<int:id>',views.retrive_student,name="retrive_student"),
    path('update_student/<int:id>',views.student_update,name="update_student"),
    path('delete_student/<int:id>',views.delete_student,name="delete_student"),
    path('courses/<int:id>/student/',views.enroll_course_student,name='enroll_course_student')


    
    
]