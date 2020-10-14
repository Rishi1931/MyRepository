from django.shortcuts import render, redirect
from .models import destination
from .models import destination1
from .models import newspost
from .models import newspage
from .models import Feedback
from .models import Subscribe
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import FeedbackForm
from .forms import SubscribeForm
from .models import Item
from django.forms import inlineformset_factory

# Create your views here.


def index(request):

    dests = destination.objects.all()
    posts = newspost.objects.all()
    obj = Item.objects.all()

    
    
    total_posts = posts.count()


    

    if request.method=='POST':
        srch = request.POST['srh']

        if srch:
            match = destination.objects.filter(Q(name__icontains=srch)| Q(price__lte=srch))


            if match:
                return render(request, "index.html", {'dests':match})

            else:
                messages.error(request, 'No Result Found')

        else:
            return redirect('/')


    sub = SubscribeForm()
    if request.method == 'POST':

            sub = SubscribeForm(request.POST)
            if sub.is_valid():
                sub.save()
            

    context = {'dests': dests, 'posts': posts, 'obj': obj,'total_posts':total_posts, 'sub':sub}
    
    return render(request, "index.html", context)



@login_required(login_url='login')
def destinations(request):
 
    dests1 = destination1.objects.all()



    sub = SubscribeForm()
    if request.method == 'POST':
            sub = SubscribeForm(request.POST)
            if sub.is_valid():
                sub.save()

    if request.method=='POST':
        srch = request.POST['srh']

        if srch:
            match = destination1.objects.filter(Q(name__icontains=srch)| Q(price__lte=srch))


            if match:
                return render(request, "destinations.html", {'dests1':match})

            else:
                messages.error(request, 'No Result Found')

        else:
            return redirect('destinations')

    context = {'dests1': dests1, 'sub':sub}
    return render(request, "destinations.html", context)


@login_required(login_url='login')
def about(request):

    subs = Subscribe.objects.all()

    sub = SubscribeForm()
    if request.method == 'POST':
            
            sub = SubscribeForm(request.POST)
            if sub.is_valid():
                sub.save()

    total_sub = subs.count()

    context = {'sub':sub, 'subs':subs, 'total_sub':total_sub}
    return render(request, "about.html", context)

@login_required(login_url='login')
def news(request):

    
    post  = newspage.objects.all()
    posts = newspost.objects.all()


    sub = SubscribeForm()
    if request.method == 'POST':
            
            sub = SubscribeForm(request.POST)
            if sub.is_valid():
                sub.save()

    context = {'post': post, 'posts': posts, 'sub':sub}
    return render(request, "news.html", context)

@login_required(login_url='login')
def contact(request):
    map = 'pk.eyJ1IjoicmlzaGlyYWozMTAiLCJhIjoiY2tmaDh3YTByMDM2dTJxbGNuNnZ6cXg2NCJ9.a9BK-4hEeEGqu4YyAfj_ow'

    
    form = FeedbackForm()
    if request.method == 'POST':
            form = FeedbackForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('contact')
               


    sub = SubscribeForm()
    if request.method == 'POST':
            sub = SubscribeForm(request.POST)
            if sub.is_valid():
                sub.save()

                messages.success(request, 'Subscribed')

            
                
    context = {'form':form, 'map':map, 'sub':sub}

    return render(request, "contact.html", context)
    

def search(request):
    obj = Item.objects.all()
    
    return render(request, "search.html", {'obj': obj})