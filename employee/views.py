from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core import serializers
import json
from django.contrib import messages
from .models import Employee,AssignWork,Reply

# Employee Login
def login(request):
    if request.method=='POST':
        email=request.POST['email']
        pwd=request.POST['pwd']
        user_count=Employee.objects.filter(email=email,emp_password=pwd).count()
        if user_count>0:
            user_data=Employee.objects.filter(email=email,emp_password=pwd)
            request.session['loginUser']=True
            request.session['userData']=serializers.serialize('json',user_data)
            return redirect('dashboard')
        else:
            messages.info(request,'Invalid Email/Password!!')
    return render(request,'login.html')

def dashboard(request):
    if request.session['loginUser']:
        decoded_data=json.loads(request.session['userData'])
        user_id=decoded_data[0]['pk']
        assigned_works=AssignWork.objects.filter(employee=user_id,work_status=False).all()
        return render(request,'dashboard.html',{
            'assigned_works':assigned_works
        })

def completed(request):
    if request.session['loginUser']:
        decoded_data=json.loads(request.session['userData'])
        user_id=decoded_data[0]['pk']
        completed_works=AssignWork.objects.filter(employee=user_id,work_status=True).all()
        return render(request,'completed-work.html',{
            'completed_works':completed_works
        })

# Assigned Work Replies
def replies(request,id):
    if request.session['loginUser']:
        work_detail=AssignWork.objects.get(pk=id)
        replies=Reply.objects.filter(work=id).all()
        return render(request,'replies.html',{
            'work_detail':work_detail,
            'replies':replies
        })
    else:
        return redirect('login')

# Add Reply
def add_reply(request,work_id):
    if request.session['loginUser']:
        work_detail=AssignWork.objects.get(pk=work_id)
        if request.method=='POST':
            reply_txt=request.POST['reply_txt']
            reply_status=request.POST['reply_status']
            replyStatus=False
            if reply_status=='1':
                replyStatus=True
                AssignWork.objects.filter(id=work_id).update(work_status=True)
            reply=Reply(work=work_detail,reply_txt=reply_txt,reply_status=replyStatus)
            reply.save()
            # Update Work also

            messages.info(request,'Reply has been added')
        # Load Data
        return render(request,'add-reply.html',{
            'work_detail':work_detail
        })
    else:
        return redirect('login')

def logout(request):
    del request.session['loginUser']
    return redirect('login')
