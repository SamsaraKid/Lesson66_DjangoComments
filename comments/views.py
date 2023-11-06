from django.shortcuts import render
from .models import *
from .forms import *



def index(req):
    return render(req, 'index.html', {'kino': Kino.objects.all()})


def film(req, id):
    kino = Kino.objects.get(id=id)
    forma = CommentForm()
    commentsall = Comment.objects.filter(active=True, kino_id=id)
    # commentsall = kino.comment_set.filter(active=True)
    if req.POST:
        forma = CommentForm(req.POST)
        if forma.is_valid():
            commentnew = Comment.objects.create()
            commentnew.name = forma.cleaned_data.get('name')
            commentnew.body = forma.cleaned_data.get('body')
            commentnew.kino = kino
            commentnew.active = True
            commentnew.save()
            forma = CommentForm()
    data = {'forma': forma, 'commentsall': commentsall, 'kino': kino}
    return render(req, 'film.html', context=data)