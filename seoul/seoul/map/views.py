from django.shortcuts import render
import json

# Create your views here.
def index(request):
    # qs = DCPOWERSTATS.objects.all().values('TS','PuE').order_by('TS')
    # # slice the queryset to hit the database and convert into list
    # context = {'data_json': json.dumps(qs[:])}
    return render(request, 'map/index.html')