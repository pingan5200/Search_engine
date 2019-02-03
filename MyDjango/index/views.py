from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from .models import *
from haystack.views import SearchView
from django.views.generic import ListView


# Create your views here.
class MySearchView(SearchView):
    template = 'search/search.html'

    def create_response(self):
        if not self.request.GET.get('q', ''):
            return redirect('index:home')
        else:
            qs = super().create_response()
            return qs


class QuestionListView(ListView):
    # 数据来源哪个表
    model = Product
    # 从数据库Question表获取所有数据列表的名字
    context_object_name = 'product_list'
    # 渲染模板
    template_name = 'index/index.html'
    # 分页，每页6个
    paginate_by = 6
