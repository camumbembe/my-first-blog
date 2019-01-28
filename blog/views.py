from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
<<<<<<< HEAD
    return render(request, 'blog/post_list.html', {})
=======
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

>>>>>>> 6f69364c20381580475ce3bfb045c3199b5fd433
