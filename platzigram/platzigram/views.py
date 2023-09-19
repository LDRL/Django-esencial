from django.http import HttpResponse

# Utilities
from datetime import datetime
import json

def hello_world(request):

    now = datetime.now().strftime('%b %dth, %y - %H:%M hrs')
    return HttpResponse('oh hi! {now}'.format(now=str(now)))

def sort_integers(request):
    lista = [int(i) for i in request.GET['numbers'].split(',')]
    lista.sort()

    data = {
        'status': 'ok',
        'numbers': lista,
        'message': 'success'
    }
    return HttpResponse(json.dumps(data), content_type='application/json')

def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! welcome to platzigram'.format(name)
    
    return HttpResponse(message) 