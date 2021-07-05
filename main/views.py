from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Category,Skill
# Create your views here.
def index(request):
    category = Category.objects.all()
    skill={}
    # print(category)
    for c in category:
        skills = Skill.objects.filter(category=c)
        
        # print(skills)
        a=list(skills)
        # print(a)
        # print(type(a))
        # print(type(skills))
        skill[c.name]=a
    # print(category)
    # print(context)
    # for i in context:
    #     # print(i)
    #     for j in context[i]:
    #         print(j.name)
    return render(request,'index.html',{'skill':skill})

