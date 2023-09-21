"""Posts views."""

# Django
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
#utilities
from datetime import datetime

posts = [
    {
        'title': 'Mont Blanc',
        'user':{
            'name': 'Yesica Cortes',
            'picture': 'https://picsum.photos/60/60/?image=1027',
        },
        'timestamp': datetime.now().strftime('%b %dth, %y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600/?image=1036',
    },
    {
        'title': 'Via Lactea',
        'user':{
            'name': 'C. Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005',
        },
        'timestamp': datetime.now().strftime('%b %dth, %y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user':{
            'name': 'Thespianartist',
            'picture': 'https://picsum.photos/60/60/?image=883',
        },
        'timestamp': datetime.now().strftime('%b %dth, %y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    },
]

@login_required
def list_posts(request):
    return render(request, 'posts/feed.html',{'posts': posts})
