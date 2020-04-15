from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
  
 
from .models import Squad
 
from django.utils import timezone


def home(request):
    squads = Squad.objects
    return render(request, 'squads/home.html', {'squads': squads})


@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            squad = Squad()
            squad.title = request.POST['title']
            squad.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                squad.url = request.POST['url']
            else:
                squad.url = 'http://' + request.POST['url']
            squad.icon = request.FILES['icon']
            squad.image = request.FILES['image']
            squad.pub_date = timezone.datetime.now()
            squad.hunter = request.user
            squad.save()
            return redirect('/squads/' + str(squad.id))
        else:
            return render(request, 'squads/create.html', {'error': 'All fields are required.'})
    else:
        return render(request, 'squads/create.html')


def detail(request, squad_id):
    squad = get_object_or_404(Squad, pk=squad_id)
    return render(request, 'squads/detail.html', {'squad': squad})


@login_required(login_url="/accounts/signup")
def upvote(request, squad_id):
    if request.method == 'POST':
        squad = get_object_or_404(Squad, pk=squad_id)
        squad.votes_total += 1
        squad.save()
        return redirect('/squads/' + str(squad.id))
