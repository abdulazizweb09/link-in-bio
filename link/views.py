from django.shortcuts import render,redirect
from django.views import View
from link.models import *
# Create your views here.
class LoginView(View):
    def get(self,request):
        return render(request,'login.html')
    
    def post(self,request):
        name=request.POST.get('name')
        password=request.POST.get('password')

        if name=='abdulaziz' and password=='2009':
            request.session['user']='admin'

            return redirect('home')
        return redirect('login')

class HomeView(View):
    def get(self,request):
        if request.session.get('user')=='admin':
            links=Links.objects.all()

            context={
                'links':links,
            }

            return render(request,'home.html',context)
        return redirect('login')
    


class AddView(View):
    def get(self,request):
        if request.session.get('user')=='admin':
            return render(request,'add.html')
        return redirect('login')
    def post(self,request):
        name=request.POST.get('name')
        img=request.FILES.get('img',None)
        tg=request.POST.get('tg')
        natg_akkme=request.POST.get('tg_akk')
        insta=request.POST.get('insta')
        youtube=request.POST.get('youtube')
        tiktok=request.POST.get('tiktok')
        link=request.POST.get('link')
        github=request.POST.get('github')

        Links.objects.create(
            name=name,
            img=img,
            tg=tg,
            tg_akk=natg_akkme,
            insta=insta,
            youtube=youtube,
            tiktok=tiktok,
            link=link,
            github=github,
        )        
        return redirect('home')

    


class DetailwView(View):
    def get(self,request,id):
        link=Links.objects.get(id=id)

        context={
            'link':link,
        }

        return render(request,'details.html',context=context)
    
    def post(self, request, id):
        link = Links.objects.get(id=id)

        name = request.POST.get('name')
        tg = request.POST.get('tg')
        tg_akk = request.POST.get('tg_akk')
        insta = request.POST.get('insta')
        youtube = request.POST.get('youtube')
        tiktok = request.POST.get('tiktok')
        link_url = request.POST.get('link')
        github = request.POST.get('github')
        img = request.FILES.get('img')

        if name:
            link.name = name
        if tg:
            link.tg = tg
        if tg_akk:
            link.tg_akk = tg_akk
        if insta:
            link.insta = insta
        if youtube:
            link.youtube = youtube
        if tiktok:
            link.tiktok = tiktok
        if link_url:
            link.link = link_url
        if github:
            link.github = github
        if img:
            link.img = img

        link.save()

        return redirect('home')
    

class DeleteView(View):
    def get(self,request,id):
        Links.objects.get(id=id).delete()

        return redirect('home')
    
class UserView(View):
    def get(self, request, slug):
        link=Links.objects.get(slug=slug)
        if not link:
            return redirect('login')
        context={
            'link':link,
        }
        return render(request,'user.html',context)