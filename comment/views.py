<<<<<<< HEAD
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from gallery.models import Artwork
from .forms import CommentForm

@login_required
def add_comment(request, artwork_id):
    artwork = get_object_or_404(Artwork, id=artwork_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.artwork = artwork
            comment.user = request.user
            comment.save()
    return redirect('gallery:gallery_list')

=======
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from gallery.models import Artwork
from .forms import CommentForm

@login_required
def add_comment(request, artwork_id):
    artwork = get_object_or_404(Artwork, id=artwork_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.artwork = artwork
            comment.user = request.user
            comment.save()
    return redirect('gallery:gallery_list')

>>>>>>> 7956767a86adae2d1e0b7eff85090f4301cedb4a
