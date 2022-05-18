from django.shortcuts import render, redirect
from django.http import HttpResponse
from dashboard.models import Course, Video
from dashboard.forms import RegistrationForm ,LoginForm
from django.views import View

# from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home(request):
    courses = Course.objects.all()  
    # print(courses)
    return render(request, template_name="dashboard\index.html",context= {"courses" : courses})

def coursePage(request,slug):
    # print(slug)
    print(request.user.is_authenticated)
    course = Course.objects.get(slug = slug)
    serial_number = request.GET.get('lecture')

    if serial_number is None:
        serial_number = 1
    video = Video.objects.get(serial_number= serial_number, course= course)
    # print(video)
    # print(serial_number,course)
    if((request.user.is_authenticated is False) and (video.is_preview is False) ):
        return redirect("login")
        # if you buied the course then only see this

    context ={
        "course" : course,
        "video" : video
    }
    return render(request, template_name="dashboard\course_page.html" , context = context)


# class SignupView(View):
#     def get(self,request):
#         form = RegistrationForm()
#         return render(request, template_name="dashboard\signup.html" , context={'form' : form})
#     def post(self, request):
#         form = RegistrationForm(request.POST)
#         if(form.is_valid()):
#             user = form.save()
#             # print(user.first_name)
#             # print(user.last_name)
#             # print(user.email)
#             if(user is not None):
#                 return redirect('login')
#         return render(request, template_name="dashboard\signup.html" , context={'form' : form})
    


def signup(request):
    if(request.method == "GET"):
        form = RegistrationForm()
        return render(request, template_name="dashboard\signup.html" , context={'form' : form})
    
    form = RegistrationForm(request.POST)
    if(form.is_valid()):
        user = form.save()
        print(user.first_name)
        print(user.last_name)
        print(user.email)
        if(user is not None):
                return redirect('login')
    return render(request, template_name="dashboard\signup.html" , context={'form' : form})
    


def login(request):
    if(request.method == "GET"):
        form = LoginForm()
        context = {
            "form" : form
        }
        return render(request, template_name="dashboard\login.html",context=context )
    elif(request.method == "POST"):
        form = LoginForm(request = request , data = request.POST)
        context = {
            "form" : form
        }
        if(form.is_valid()):
            redirect('home')
            # return HttpResponse("Login Form Submitted")
        return render(request, template_name="dashboard\login.html",context=context )
        





def signout(request):
    return HttpResponse("LogOut")

def checkout(request , slug):

    return render(request, "dashboard\payment.html")

