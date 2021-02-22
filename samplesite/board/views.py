from django.shortcuts import render, redirect
from .models import Board, Rubric
from .forms import BoardForm, SearchForm
from django.core.paginator import Paginator
from django.db.models.query_utils import Q


def index(request):
    form = SearchForm()
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
    context = {'bs': page.object_list, 'page': page, 'rubrics': rubrics, 'pages': pages, 'search_form': form}
    return render(request, 'board/index.html', context)


def by_rubric(request, rubric_id):
    form = SearchForm
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
    context = {'bs': page.object_list, 'page': page, 'rubrics': rubrics, 'current_rubric': current_rubric, 'pages': pages, 'search_form': form}
    return render(request, 'board/by_rubric.html', context)


def add_ad(request):
    search_form = SearchForm
    if request.method == 'POST':
        form = BoardForm(request.POST, request.FILES)
        if form.is_valid():
            if 'image' in request.FILES:
                form.image = request.FILES['image']
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('index')
    else:
        form = BoardForm()
        rubrics = Rubric.objects.all()
        return render(request, 'board/create.html', {'form': form, 'rubrics': rubrics, 'search_form': search_form})


def show_user_posts(request):
    form = SearchForm
    user_posts = Board.objects.filter(user=request.user)
    rubrics = Rubric.objects.all()
    context = {'bs': user_posts, 'rubrics': rubrics, 'search_form': form}
    return render(request, 'board/index.html', context)


def search(request):
    if 'keyword' in request.GET and request.GET['keyword']:
        form = SearchForm(request.GET)
        if form.is_valid():
            rubrics = Rubric.objects.all()
            cd = form.cleaned_data
            query = Q(title__icontains=cd['keyword']) | Q(content__icontains=cd['keyword'])
            results = Board.objects.filter(query)
            total_results = results.count()
            return render(request, 'board/search.html', {'search_form': SearchForm(), 'cd': cd, 'results': results, 'total_results': total_results, 'rubrics': rubrics})
    else:
        return redirect('index')


def delete_ad(request, ad_id):
    deleted_ad = Board.objects.filter(id=ad_id)
    deleted_ad.delete()
    return redirect('index')
