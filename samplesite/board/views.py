from django.http import HttpResponse
from .models import Board


def index(request):
    s = 'Список объвлений\r\n\r\n\r\n'
    for b in Board.objects.order_by('-published'):
        s += b.title + '\r\n' + b.content + '\r\n\r\n'
    return HttpResponse(s, content_type='text/plain; charset=utf-8')