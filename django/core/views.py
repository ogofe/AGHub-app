from django.shortcuts import render
from .models import Sermon



# Create your views here.
def index_view(request):
    return render(request, 'core/index.html', {'title': 'Home'})

def sermons_view(request):
    sermons = Sermon.objects.all()
    context= {
        'sermons': sermons,
        'title' : 'Sermons'
    }
    return render(request, 'core/sermons.html', context)