from django.shortcuts import render


posts = [
    {
        'author': 'RennyCodes',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 27, 2024'
    },
    {
        'author': 'RennyAI',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'January 28, 2024'
    }
]


# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

