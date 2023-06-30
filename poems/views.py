from django.shortcuts import render, redirect
from .models import Poem, Review
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
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


@login_required
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
        

@login_required
def updatereview(request, id):
    review = get_object_or_404(Review,pk=id,user=request.user)
    if request.method == 'GET':
        form = ReviewForm(instance=review)
        return render(request, 'updatereview.html', {'review': review,'form':form})
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
            return redirect('poem_detail', review.poem.id)
        except ValueError:
            return render(request,'updatereview.html',{'review': review,'form':form,'error':'Bad data in form'})
        

@login_required
def deletereview(request, id):
    review = get_object_or_404(Review, pk=id,user=request.user)
    review.delete()
    return redirect('poem_detail', review.poem.id)