from django.urls import path
from . import views

app_name = 'index'
urlpatterns = [
    path('search/', views.MySearchView(), name='haystack'),
    path('', views.QuestionListView.as_view(), name='home')
]
