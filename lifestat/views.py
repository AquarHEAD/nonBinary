# Create your views here.
from django.shortcuts import render_to_response
from nonBinary.lifestat.models import Stat

def home(request):
    latest_stats = Stat.objects.all().order_by('-stat_date')
    return render_to_response('lifestat/home.html',{'latest_stats': latest_stats})