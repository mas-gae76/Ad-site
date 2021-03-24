from rest_framework import generics
from ..models import Board
from .serializers import BoardSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action


class BoardListView(generics.ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class BoardDetailView(generics.RetrieveAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class BoardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    @action(methods=['post'], detail=True)
    def enroll(self, request, *args, **kwargs):
        board = self.get_object()
        board.save()
        return Response({'enrolled': True})
