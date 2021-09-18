from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentReg
from .models import Student
from django.contrib import messages

# Create your views here.
# This function will add new itm and show all items 
def add_show(request):
    if request.method == 'POST':
        fm = StudentReg(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = Student(name=nm, email=em, password=pw)
            if len(nm)<2 or len(em)<3 or len(pw)<5:
                messages.error(request, "please fil data correctly")
            else: 
                reg.save()
                fm = StudentReg()
                messages.success(request, "data submitted successfully.")
    else:
            fm = StudentReg()
    stud = Student.objects.all()
    return render(request, 'enroll/addnshow.html', {'form':fm,'stu':stud})   

# This function will Update/Edit

def update_data(request, id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        fm = StudentReg(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'data updated successfully.')
    else:
     pi = Student.objects.get(pk=id)
     fm = StudentReg(instance=pi)
    messages.success(request, 'welcome to Update page')      
    return render(request, 'enroll/updatestudent.html', {'form':fm})
    



    # This function will delete item

def delete_data(request, id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        pi.delete()
    messages.success(request, 'Entry deleted Successfully')    
    return HttpResponseRedirect('/')
         





