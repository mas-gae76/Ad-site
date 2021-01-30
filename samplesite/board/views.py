from django.shortcuts import render
from .models import Board, Rubric
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import BoardForm
from django.core.paginator import Paginator


def index(request):
    bs = Board.objects.all()
    rubrics = Rubric.objects.all()
    paginator = Paginator(bs, 5)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {'bs': page.object_list, 'page': page, 'rubrics': rubrics}
    return render(request, 'board/index.html', context)


def by_rubric(request, rubric_id):
    bs = Board.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    paginator = Paginator(bs, 5)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {'bs': page.object_list, 'page': page,'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'board/by_rubric.html', context)


class BoardCreateView(CreateView):
    template_name = 'board/create.html'
    form_class = BoardForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
