# blog/urls.py
from django.urls import path
from .views import (
    PostListView, post_detail_view , PostCreateView,
    PostUpdateView, PostDeleteView, post_empty_view,home_view
)

urlpatterns = [
    path('', home_view, name='home'),
    path('publicaciones/', PostListView.as_view(), name='post_list'),
    path('nuevo/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/', post_detail_view, name='post_detail'),
    path('<int:pk>/editar/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/borrar/', PostDeleteView.as_view(), name='post_delete'),
    path('vacio/', post_empty_view, name='post_empty'),
]

