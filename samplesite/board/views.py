from django.shortcuts import render
from .models import Board, Rubric


def index(request):
    bs = Board.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bs': bs, 'rubrics': rubrics}
    return render(request, 'board/index.html', context)


def by_rubric(request, rubric_id):
    bs = Board.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bs': bs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'board/by_rubric.html', context)
