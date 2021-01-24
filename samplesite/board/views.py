from django.shortcuts import render
from .models import Board


def index(request):
    bs = Board.objects.all()
    return render(request, 'board/index.html', {'bs': bs})