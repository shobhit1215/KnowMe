from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Category,Skill,Project,Background,Visitor
from django.contrib import messages
# Create your views here.
def index(request):
    category = Category.objects.all()
    skill={}
    project={}
    
    # print(category)
    for c in category:
        skills = Skill.objects.filter(category=c)
        projects = Project.objects.filter(category=c)
        backgrounds = Background.objects.all()
    
        
        # print(skills)
        a=list(skills)
        b=list(projects)
        # print(a)
        # print(type(a))
        # print(type(skills))
        skill[c.name]=a
        project[c.name]=b
    # print(category)
    # print(context)
    # for i in context:
    #     # print(i)
    #     for j in context[i]:
    #         print(j.name)
    if request.method=='POST':
        if request.POST.get('Name') and request.POST.get('Email'):
            print(request.POST)
            visitor = Visitor()
            visitor.name=request.POST.get('Name')
            visitor.email=request.POST.get('Email')
            visitor.message=request.POST.get('Message')
            visitor.save()
            messages.success(request, 'Thanks for your Response. I will contact you shortly')
        else:
            messages.success(request, 'Fill the details.')
    return render(request,'index.html',{'skill':skill,'project':project,'backgrounds':backgrounds})

