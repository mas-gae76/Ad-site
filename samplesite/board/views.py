from django.shortcuts import render, redirect
from .models import Board, Rubric
from .forms import BoardForm
from django.core.paginator import Paginator


def index(request):
    bs = Board.objects.all()
    rubrics = Rubric.objects.all()
    paginator = Paginator(bs, 10)
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
    paginator = Paginator(bs, 10)
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


def add_ad(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('index')
    else:
        form = BoardForm()
        return render(request, 'board/create.html', {'form': form})


def show_user_posts(request):
    user_posts = Board.objects.filter(user=request.user)
    context = {'posts': user_posts}
    return render(request, 'user_posts.html', context)
