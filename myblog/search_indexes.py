# coding=utf-8

from haystack import indexes
from myblog.models import blog


class blogIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    #title = indexes.CharField(model_attr='gtitle')
    #intro = indexes.CharField(model_attr='gintro')
    #content = indexes.CharField(model_attr='gcontent')

    def get_model(self):
        return blog

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()