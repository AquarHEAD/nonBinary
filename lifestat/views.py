# Create your views here.
from django.shortcuts import render_to_response
from datetime import datetime
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from nonBinary.lifestat.models import Stat, StatForm

def home(request):
    stats = Stat.objects.all().order_by('-stat_date')
    form = StatForm()
    paginator = Paginator(stats, 13)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    
    try:
        latest_stats = paginator.page(page)
    except (EmptyPage, InvalidPage):
        latest_stats = paginator.page(paginator.num_pages)
    return render_to_response('lifestat/home.html',{'latest_stats': latest_stats, 'new_stat_form': form},
                              context_instance=RequestContext(request))

def new(request):
    f = StatForm(request.POST)
    new_stat = f.save(commit=False)
    new_stat.stat_date = datetime.now()
    new_stat.save()
    return HttpResponseRedirect('/')

def delete(request, stat_id):
    f = Stat.objects.get(pk=stat_id)
    f.delete()
    return HttpResponseRedirect('/')
    