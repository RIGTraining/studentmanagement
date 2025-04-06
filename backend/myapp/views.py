from django.shortcuts import render,redirect
from django.views.generic import TemplateView, View, CreateView, DetailView,FormView
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from.forms import *
from.models import *
# Create your views here.


class Homepage(View):
    def get(self, request):
        return render(request, 'Homepage.html')
    
class TrainerView(View):
    def get(self, request):
        trainers = Trainers.objects.all()
        context ={'trainers':trainers}
        return render(request, 'Trainer.html', context)
    
class CreateTrainer(View):
    def get(self, request):
        fm = TrainersCreateForm()
        trainers = Trainers.objects.all()
        context = {'fm':fm, 'trainers':trainers}
        return render(request, 'CreateTrainer.html', context)
    
    def post(self, request):
        fm = TrainersCreateForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            return redirect(request.META['HTTP_REFERER'])
        

class CoursesView(View):
    def get(self, request):
        fm = CourseCreateForm()
        courses = Courses.objects.all()
        context = {'fm':fm, 'courses':courses}
        return render(request, 'CoursesView.html', context)
    
    def post(self, request):
        fm = CourseCreateForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect(request.META['HTTP_REFERER'])
        
        else:
            print('error have')
            return redirect(request.META['HTTP_REFERER'])


class RegisterStudent(View):
    def get(self, request):
        reg = UserRegister()
        context ={'reg':reg}
        return render(request, 'Register.html', context)
    
    
    def post(self, request):
        fm = UserRegister(request.POST)
        if fm.is_valid():
            # fm.save()
            
            return redirect('/')
        
        else:
            print('error have')
            return redirect(request.META['HTTP_REFERER'])


class ULoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())        

class UserLoginView(FormView):
    template_name = 'Login.html'
    form_class = ULoginForm
    success_url = reverse_lazy('Homepage')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data['password']
        # print(username, password)
        usr = authenticate(username=username, password=password)
        # print(usr)
        if usr is not None:
            login(self.request, usr)

        else:
            print('error have')
            return render(self.request, self.template_name, {'form': self.form_class, 'error': 'Invalid user login!'})
        return super().form_valid(form)
        
class UserLogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('UserLoginView')



# School 
class Dashboard(View):
    def get(self, request):
        ac = ClassName.objects.all()
        courses = Courses.objects.all()
        trainers = Trainers.objects.all()
        courseform = CourseCreateForm()
        classfm = ClassNameForm()
        context = {'ac':ac, 'courses':courses, 'trainers':trainers, 'courseform':courseform, 'classfm':classfm}
        return render(request, 'school/Dashboard.html', context)
    
class StudentList(View):
    def get(self, request):
        st = User.objects.filter(is_staff = False)
        context ={'st':st}
        return render(request, 'school/StudentList.html', context)
    
class ClassList(View):
    def get(self, request):
        ac = ClassName.objects.all()
        context = {'ac':ac}
        return render(request, 'school/ClassList.html', context)