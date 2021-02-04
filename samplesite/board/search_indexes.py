from haystack import indexes
from .models import Board


class BoardIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    publish = indexes.DateTimeField(model_attr='publish')

    def get_model(self):
        return Board

    def index_queryset(self, using=None):
        return self.get_model().published.all()
