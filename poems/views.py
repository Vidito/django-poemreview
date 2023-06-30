from django.shortcuts import render, redirect
from .models import Poem, Review
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .forms import ReviewForm
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
    reviews = Review.objects.filter(poem = poem)
    context = {'poem': poem, 'title': poem.title, 'reviews': reviews}
    return render(request, 'poem_detail.html', context)


def createreview(request, id):
    poem = get_object_or_404(Poem, id=id)
    if request.method == 'GET':
        return render(request, 'createreview.html', {'title': 'Create Review', 'poem': poem, 'form':ReviewForm})
    else:
        try:
            form = ReviewForm(request.POST)
            if form.is_valid():
                newReview = form.save(commit=False)
                newReview.user = request.user
                newReview.poem = poem
                newReview.save()
                return redirect('poem_detail', id=newReview.poem.id)
        except ValueError:
            return render(request, 'createreview.html', {'form':ReviewForm, 'error':'Bad data passed in'})