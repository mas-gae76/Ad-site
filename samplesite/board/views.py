from django.shortcuts import render
from .models import Board


def index(request):
    bs = Board.objects.order_by('-published')
    return render(request, 'board/index.html', {'bs': bs})