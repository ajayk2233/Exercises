from django.shortcuts import render,HttpResponse
from .models import School
# Create your views here.
def choose(request):
    return render(request,'choose.html')

def show_data(request):
    name = request.POST.get('name')
    roll_no = request.POST.get('roll_no')
    gender = request.POST.get('gender')
    phone = request.POST.get('phone')
    school = School.objects.all()
    
    context = {'school':school,
                name:name,roll_no:roll_no,gender:gender,phone:phone}
    return render(request,'show.html',context)