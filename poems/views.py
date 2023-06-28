from django.shortcuts import render
from .models import Poem
from django.shortcuts import get_object_or_404
from django.db.models import Q
# Create your views here.


def home(request):
    poems = Poem.objects.all().order_by('-id')
    if request.GET.get('qp', None):
        qp = request.GET['qp']
        poems = poems.filter(Q(title__icontains=qp) | Q(author__icontains=qp))
 
    context = {'poems': poems, 'title': 'Home Page', 'count':poems.count()}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html', {'title': 'About Page'})


def poem_detail(request, id):
    poem = get_object_or_404(Poem, id=id)
    context = {'poem': poem, 'title': poem.title}
    return render(request, 'poem_detail.html', context)