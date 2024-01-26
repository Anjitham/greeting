from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class GoodMorningView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"morning.html")
    
class GoodEveningView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"evening.html")
    
class GoodAfternoonview(View):
    def get(self,request,*args,**kwargs):
        return render(request,"afternoon.html")
    
class GoodNightview(View):
    def get(self,request,*args,**kwargs):
        return render(request,"night.html")
    
class HappyBirthdayview(View):
    def get(self,request,*args,**kwargs):
        return render(request,"birthday.html")
