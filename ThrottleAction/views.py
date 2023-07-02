from django.shortcuts import render,redirect
from .models import Reviews,Bikes,Exclusive,Mailletter,Contact
# Create your views here.
def index(request):
     context={}
     context['reviewlist']=Reviews.objects.order_by("created_on").reverse()
     return render(request,'index.html',context)

def showreview(request,slug):
     context={}
     post = Reviews.objects.filter(slug=slug).first()
     context={'post': post,'user':request.user}
     return render(request,'article.html',context)

def showexclusive(request,slug):
     context={}
     post = Exclusive.objects.filter(slug=slug).first()
     context={'post': post,'user':request.user}
     return render(request,'blog.html',context)

def exclusive(request):
     context={}
     context['exclusivelist']=Exclusive.objects.order_by("created_on").reverse()
     return render(request,'exclusive.html',context)

def about(request):
     return render(request,'about.html')

def review(request):
     context={}
     context['reviewlist']=Reviews.objects.order_by("created_on").reverse()
     return render(request,'review.html',context)

def privacy(request):
     return render(request,'privacy.html')

def terms(request):
     return render(request,'terms.html')

def consult(request):
     return render(request,'consult.html')

def contact(request):
     return render(request,'contact.html')

def showreview(request,slug):
     context={}
     post = Reviews.objects.filter(slug=slug).first()
     context={'post': post,'user':request.user}
     return render(request,'article.html',context)

def contactform(request):
     if request.method == "POST":
        Name = request.POST.get('name')
        Mobile = request.POST.get('pno')
        Email=request.POST.get('mailid')
        Question = request.POST.get('question')
        comment=Contact(Name=Name,Mobile=Mobile,Email=Email,Question=Question)
        comment.save()
     
     return redirect(f"/contact")

def subscribe(request):
     if request.method == "POST":
        mail=request.POST.get('email')
        comment=Mailletter(mail= mail,)
        comment.save()
     
     return redirect(f"/")


def error_400(request):
        data = {}
        return render(request,'400.html', data)

def error_403(request):
        data = {}
        return render(request,'403.html', data)

def error_404(request):
        data = {}
        return render(request,'404.html', data)

def error_500(request):
        data = {}
        return render(request,'500.html', data)