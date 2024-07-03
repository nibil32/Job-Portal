from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,TemplateView,DetailView,UpdateView,ListView
from jobseeker.forms import Registration,Studentprofile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from myapp.models import Applications, student
from myapp.models import job
from django.utils.decorators import method_decorator
# Create your views here.


def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        else:
            return fn(request,*args,**kwargs)
    return wrapper    

class Register(CreateView):
    template_name="jobseeker/register.html"
    form_class=Registration
    model=User
    success_url = reverse_lazy("signin")


# class Signin(View):
#     def get(self,request,*args,**kwargs):
#         form=Loginform()
#         return render(request,"jobseeker/login.html",{"form":form})
    
#     def post(self,request,*args,**kwargs):
#         form=Loginform(request.POST)
#         if form.is_valid():
#             u_name=form.cleaned_data.get("username")
#             pwd=form.cleaned_data.get("password")
#             user_obj=authenticate(request,username=u_name,password=pwd)
#             if user_obj:
#                 login(request,user_obj)
#                 return redirect
#             else:
#                 print("false dredentials")
#         return redirect("reg")

class Student_home(ListView):
    template_name="jobseeker/index.html"
    model=job
    context_object_name="job"

class Jobseeker_profile(CreateView):
    template_name="jobseeker/profile.html"
    form_class=Studentprofile
    model=student
    success_url=reverse_lazy("reg")

    # def post(self,request,*args,**kwargs):
    #     form=Studentprofile(request.POST,files=request.FILES)
    #     if form.is_valid():
    #         form.istance.user=request.user
    #         form.save()
    #         return redirect("seekerindex")
    #     else:
    #         print("get out")
    #     return redirect("reg")
    def form_valid(self, form: BaseModelForm):
        form.instance.user=self.request.user
        return super().form_valid(form)

class Profileview(DetailView):
    template_name="jobseeker/p_view.html"
    context_object_name="data"
    model=student
    success_url=reverse_lazy("view")
    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     qs=student.objects.filter(id=id)
    #     return render(request,"jobseeker/p_view.html",{"data":qs})

class update_profile(UpdateView):
    template_name="jobseeker/Profile_edit.html"
    model=student
    form_class=Studentprofile
    success_url=reverse_lazy("seekerindex")    
    
class signout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")
    
class Jobdetailview(DetailView):
    template_name="jobseeker/job_detail.html"
    model=job
    context_object_name="data"


#lh:8000/job_apply/1        urls.py   urlname/<int:pk>
@method_decorator(signin_required,name="dispatch")
class Job_apply(View):
    def get(self,request,*args,**kwargs):   
        id=kwargs.get("pk")     
        data=job.objects.get(id=id)   
        Applications.objects.create(jobs=data,student=request.user)
        return redirect("seekerindex")
    
class Applied_jobs(View):
    def get(self,request,*args,**kwargs):
        data=Applications.objects.filter(student=request.user)
        return render(request,"jobseeker/jobapplied.html",{"data":data})
    
class Delete_job(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Applications.objects.get(id=id).delete()
        return redirect("seekerindex")




