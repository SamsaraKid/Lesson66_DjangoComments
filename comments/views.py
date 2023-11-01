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
        commentnew = Comment.objects.create()
        commentnew.name = req.POST.get('name')
        commentnew.body = req.POST.get('body')
        commentnew.kino = kino
        commentnew.save()
    data = {'forma': forma, 'commentsall': commentsall, 'kino': kino}
    return render(req, 'film.html', context=data)