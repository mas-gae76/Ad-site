from django.shortcuts import render
from .models import Board, Rubric
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import BoardForm
from django.core.paginator import Paginator


def index(request):
    bs = Board.objects.all()
    rubrics = Rubric.objects.all()
    paginator = Paginator(bs, 7)
    num_pages = paginator.num_pages
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    if num_pages < 11 or page.number < 6:
        pages = [x for x in range(1, min(num_pages + 1, 11))]
    elif page.number > num_pages - 6:
        pages = [x for x in range(num_pages - 10, num_pages + 1)]
    else:
        pages = [x for x in range(num_pages - 5, num_pages + 6)]
    context = {'bs': page.object_list, 'page': page, 'rubrics': rubrics, 'pages': pages}
    return render(request, 'board/index.html', context)


def by_rubric(request, rubric_id):
    bs = Board.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    paginator = Paginator(bs, 2)
    num_pages = paginator.num_pages
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    if num_pages < 11 or page.number < 6:
        pages = [x for x in range(1, min(num_pages + 1, 11))]
    elif page.number > num_pages - 6:
        pages = [x for x in range(num_pages - 10, num_pages + 1)]
    else:
        pages = [x for x in range(num_pages - 5, num_pages + 6)]
    context = {'bs': page.object_list, 'page': page, 'rubrics': rubrics, 'current_rubric': current_rubric, 'pages': pages}
    return render(request, 'board/by_rubric.html', context)


class BoardCreateView(CreateView):
    template_name = 'board/create.html'
    form_class = BoardForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
