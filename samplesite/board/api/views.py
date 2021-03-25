from rest_framework import generics
from ..models import Board
from .serializers import BoardSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import BasePermission


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

    @action(methods=['get'], detail=True)
    def contents(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class IsEnrolled(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.filter(id=request.user.id).exists()
