from django.shortcuts import render,redirect
from django.views.generic import TemplateView, View, CreateView, DetailView,FormView
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import JsonResponse
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

class Dashboard(View):
    def get(self, request):
        ac = ClassName.objects.all()
        courses = Courses.objects.all()
        trainers = Trainers.objects.all()
        context = {'ac':ac, 'courses':courses, 'trainers':trainers}
        return render(request, 'school/index.html', context)