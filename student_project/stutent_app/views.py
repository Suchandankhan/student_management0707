from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import course,student



def index(request):
    return HttpResponse("index page")

#create

@csrf_exempt
def create_course(request):
    if request.method=="POST":
        data=json.loads(request.body)
        print(data)
    Courses=course(id=data['id'],course_name=data['course_name'], course_trainer=data['course_trainer'],course_duration=data['course_duration'],course_fees=data['course_fees'])
    Courses.save()
    return HttpResponse('created')


#retrive Course_details
def retrive_course(request,id):
    try:
        Courses=course.objects.get(id=id)
        if Courses is not None:
            return JsonResponse({"course_name":Courses.course_name,
                                 "course_trainer":Courses.course_trainer,
                                 "course_duration":Courses.course_duration,
                                 "course_fees":Courses.course_fees,})
    except:
        return HttpResponse("User id is not exist")

#update
@csrf_exempt
def update_course(request,id):
    if request.method=="POST":
        data=json.loads(request.body)
        try:
            Courses=course.objects.get(id=id)
            if Courses:
                co=course(id=data['id'],course_name=data['course_name'],course_trainer=data['course_trainer'],course_duration=data['course_duration'],course_fees=data['course_fees'])
                print(co.id)
                co.save()
                return HttpResponse("record updated sucessfully")
        except:
            return HttpResponse("record is not found")
    else:
        return HttpResponse("enter right records")
    
#delete

@csrf_exempt
def delete_course(request,id):
    try:
        if request.method=="DELETE":
            Courses=course.objects.get(id=id)
            Courses.delete()
            return HttpResponse("record Deleted")
    except:
        return HttpResponse("record does not exit")
    
    
#student create
@csrf_exempt
def create_student(request,id):
    try:
        if request.method=="POST":
            data=json.loads(request.body)
            print(data)
            print(data['id'])
            stu=student(id=data['id'],name=data['name'],
                    father_name=data['father_name'],
                    phone=data['phone'],
                    email_id=data['email_id'],
                    Courses=course.objects.get(id=id))
            stu.save()
        return HttpResponse("Created student details")
    except:
        return HttpResponse("enter course id is not exist")
    
#student retrive/

def retrive_student(request,id):
    try:
        stu=student.objects.get(id=id)
        return JsonResponse({ 
                                 "id":stu.id,
                                 "name":stu.name,
                                 "father_name":stu.father_name,
                                 "phone":stu.phone,
                                 "email_id":stu.email_id,
                                 "course":stu.Courses.course_name})
    except:
        return HttpResponse ("student is not exists")
    
#student update/
@csrf_exempt
def student_update(request,id):
    if request.method=="POST":
        data=json.loads(request.body)
        print(data)
        try:
            stu=student.objects.get(id=id)
            stu.name=data['name']
            stu.father_name=data['father_name']
            stu.phone=data['phone']
            stu.email_id=data['email_id']
            stu.Courses.course_name=data['courses']
            stu.save()
            return HttpResponse("student record updated successfully")
        except:
            return HttpResponse("student record are not found")
    else:
        return HttpResponse("enter correct record")
    
    
@csrf_exempt
def delete_student(request,id):
    try:
        if request.method=="DELETE"   :
            stu=student.objects.get(id=id)
            stu.delete()
            return HttpResponse("record deleted")
    except:
        return HttpResponse("record does not exists")
    
    
#courses/{01}/students
def enroll_course_student(request,id):
    try:
        co=course.objects.get(id=id)
        stu=student.objects.filter(Courses_id=co.id)
        l1=[]
        for i in stu:
            l1.append(dict(name=i.name,father_name=i.father_name,phone=i.phone))
        return JsonResponse({"course":co.course_name,"Responce":l1})
    except:
        return HttpResponse("course are not exist")    

    
        
# Create your views here.
"""Student Management system s/
       1. Student Create
       2.Student """