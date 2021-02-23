from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('private/', views.PostListPrivateView.as_view(), name='post_list_private'),
    path('post/<int:post_id>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:post_id>/edit/', views.PostEditView.as_view(), name='post_edit'),
    path('post/new/', views.PostNewView.as_view(), name='post_new'),
]