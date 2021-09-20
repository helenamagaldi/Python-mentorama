from django.shortcuts import render


posts = [
    {
        'author': 'helenaMagaldi',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 21, 2021',
    },
    {
        'author': 'helenaMagaldi12',
        'title': 'Blog Post 12',
        'content': '12st post content',
        'date_posted': 'August 22, 2021',
    },
    {
        'author': 'helenaMagaldi13',
        'title': 'Blog Post 13',
        'content': '13th post content',
        'date_posted': 'August 23, 2021',
    }
]

def home(request):
    context = {
        "posts": posts
    }
    # return render template instead of our http response
    # takes request as param: object
    # still returns an http response in the background
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

#  loading the template, render it and pass it to the httpresponse: django.shortcuts module helps with render
