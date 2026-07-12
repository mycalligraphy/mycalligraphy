from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Artwork, Category
from comment.models import Comment
from comment.forms import CommentForm

def gallery_view(request):
    query = request.GET.get('q')
    category_slug = request.GET.get('category')
    
    artworks_list = Artwork.objects.all().order_by('-created_at')
    
    if category_slug:
        artworks_list = artworks_list.filter(category__slug=category_slug)
    
    if query:
        artworks_list = artworks_list.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    
    paginator = Paginator(artworks_list, 6)
    page_number = request.GET.get('page')
    artworks = paginator.get_page(page_number)
    
    # اضافه کردن نظرات به هر اثر
    for artwork in artworks:
        artwork.comments_list = artwork.comments.filter(is_active=True)[:5]
    
    return render(request, 'gallery/gallery.html', {
        'artworks': artworks,
        'query': query,
        'categories': Category.objects.all(),
        'selected_category': category_slug,
    })


@csrf_exempt
def like_artwork(request, artwork_id):
    if request.method == 'POST':
        artwork = get_object_or_404(Artwork, id=artwork_id)
        artwork.likes += 1
        artwork.save()
        return JsonResponse({'likes': artwork.likes})
    return JsonResponse({'error': 'Invalid request'}, status=400)


def view_artwork(request, artwork_id):
    artwork = get_object_or_404(Artwork, id=artwork_id)
    artwork.views += 1
    artwork.save()
    return JsonResponse({'views': artwork.views})