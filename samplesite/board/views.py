from django.shortcuts import render, redirect
from .models import Board, Rubric
from .forms import BoardForm, SearchForm
from django.core.paginator import Paginator
from django.db.models.query_utils import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BoardSerializer
from rest_framework.authentication import SessionAuthentication


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
            return render(request, 'board/create.html', {'form': form, 'search_form': SearchForm})
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


@login_required
def edit_ad(request, ad_id):
    ad = get_object_or_404(Board, pk=ad_id, user=request.user)
    if request.method == 'POST':
        form = BoardForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.is_edited = True
            ad.save()
            messages.add_message(request, messages.SUCCESS, 'Объявление исправлено')
            return redirect('index')
    else:
        form = BoardForm(instance=ad)
    return render(request, 'board/edit.html', {'form': form, 'rubrics': Rubric.objects.all, 'search_form': SearchForm})


def show_user_profile(request, user_id):
    ads = Board.objects.filter(user=user_id)
    return render(request, 'board/user_profile.html', {'ads': ads, 'rubrics': Rubric.objects.all, 'search_form': SearchForm})


class CsrfExemptSessionAuth(SessionAuthentication):
    def enforce_csrf(self, request):
        return None


class BoardView(APIView):
    authentication_classes = (CsrfExemptSessionAuth,)
    queryset = None
    def get(self, request):
        bs = Board.objects.all()
        serializer = BoardSerializer(bs, many=True)
        return Response({'boards': serializer.data})

    def post(self, request):
        board = request.data.get('board')
        serializer = BoardSerializer(data=board)
        if serializer.is_valid(raise_exception=True):
            board_saved = serializer.save()
        return Response({'success': "Board '{}' published successfully".format(board_saved.title)})

    def put(self, request, pk):
        saved_board = get_object_or_404(Board.objects.all(), pk=pk)
        data = request.data.get('board')
        serializer = BoardSerializer(instance=saved_board, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            board_saved = serializer.save()
            return Response({'success': "Board '{}' updated successfully".format(board_saved.title)})

    def delete(self, request, pk):
        board = get_object_or_404(Board.object.all(), pk=pk)
        board.delete()
        return Response({'message': "Board with id '{}' has been deleted".format(pk)}, status=204)
