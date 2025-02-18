from django.shortcuts import render
from django.http import HttpResponse
from .models import people
def add(request):
    return render(request,"Adddetails.html")
def insert(request):
    p=people(name=request.POST["name"],age=request.POST["age"],email=request.POST["email"],mplace=request.POST["mplace"],mdate=request.POST["mdate"],cpn1=request.POST["cpn1"],cpnum1=request.POST["cpnum1"],cpn2=request.POST["cpn2"],cpnum2=request.POST["cpnum2"],fn=request.POST["fn"],mn=request.POST["mn"],gn=request.POST["gn"],district=request.POST["district"],state=request.POST["state"],passwd=request.POST["passwd"],image=request.FILES["img"])
    p.save()
    return render(request,"Adddetails.html")
def remove(request):
    return render(request,"removepeople.html")
def delete(request):
    id=request.POST["id"]
    passwd=request.POST["passwd"]
    p=people.objects.get(id=id)
    if(p.passwd==passwd):
        p.delete()
        return HttpResponse("success")
    else:
        return HttpResponse("error")
def search(request):
    return render(request,"searchpeople.html")
def show(request):
    count=1
    #count=request.POST["count"]
    n=12
    l=[]
    l.append(request.POST["name"])
    """l.append(request.POST["age"])
    l.append(request.POST["email"])
    l.append(request.POST["mplace"])
    l.append(request.POST["mdate"])
    l.append(request.POST["cpn"])
    l.append(request.POST["cpnum"])
    l.append(request.POST["fn"])
    l.append(request.POST["mn"])
    l.append(request.POST["gn"])
    l.append(request.POST["district"])
    l.append(request.POST["state"])"""
    j=0
    v=[]
    res=[]
    index=[]
    val=[]
    for i in l:
        if i!="na":
            v.append(j)
        j=j+1
    for i in v:
        res.append(get(i,l[i]))
    for i in range(len(res)):
       for k in res[i]:
         if k not in val:
          for j in range(len(res)):
            if k in res[j]:
                if k in val :
                    index[len(index)-1]=index[len(index)-1]+1
                else:
                    index.append(i)
                    val.append(k)
    r=[]
    for i in range(len(index)):
        j=index.index(max(index))
        index[j]=-1
        r.append(val[j])
    #return HttpResponse("ok")
    k=1
    for i in r:
       if(i!=None):
         k=None
    return render(request,"show.html",{"key":r,"k":k,"v":request.POST["name"]})

def get(i,str):
    if(i==0):
        try :
           return people.objects.filter(name=str)
        except :
            return [None]
    if(i==1):
        try:
           return people.get(age=str)
        except:
            return [None]
    if(i==2):
        try:
          return people.get(email=str)
        except:
            return [None]
    if(i==3):
        try:
          return people.get(mplace=str)
        except:
            return [None]
    if(i==4):
        try:
         return people.get(mdate=str)
        except:
            return [None]
    if(i==5):
        try:
          p1=people.get(cpn1=str)
        except:
          p1=None
        try:
          p2=people.get(cp2=str)
        except:
          p2=None
        if(p1!=None):
            return p1
        if(p2!=None):
            return p2
    if(i==6):
        try:
          p1=people.get(cpnum1=str)
        except:
          p1=None
        try:
          p2=people.get(cpnum2=str)
        except:
          p2=None
        if(p1!=None):
          return p1
        if(p2!=None):
          return p2
    if(i==7):
        try:
          return people.get(fn=str)
        except:
          return [None]
    if(i==8):
        try:
         return people.get(mn=str)
        except:
         return [None]
    if(i==9):
        try:
         return people.get(gn=str)
        except:
         return [None]
    if(i==10):
        try:
         return people.get(district=str)
        except:
         return [None]
    if(i==11):
        try:
         return people.get(state=str)
        except:
         return [None]
def showpeople(request,id):
   p=people.objects.get(id=id)
   return render(request,"showdetail.html",{"key":p})
def home(request):
   p=people.objects.all().order_by("mdate")[:8]
   return render(request,"index.html",{"key":p})
def aboutus(request):
   return render(request,"aboutus.html")
