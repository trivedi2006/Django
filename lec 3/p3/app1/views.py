from django.shortcuts import render
from app1.models import Student
# Create your views here.
def Home(request):
    return render(request,'Home.html')
def About(request):
    return render(request,'About.html')

def Nav(request):
    # name='B1'
    # score=5
    # l=[1,2,'k',145,'p']
    # d={'name':['A','B'],'run':[96,97]}
    students=Student.objects.all()
    # return render(request,"Nav.html",{'n':name,'s':score,'l':l,'d':d})
    search_term = request.GET.get('search')
    if search_term:
        students=Student.objects.filter(name__icontains=search_term)
    else:
        students=Student.objects.all()
    return render(request,"Nav.html",{"students":students})