from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:id>/detail/', views.detail, name='detail'),
    path('<int:id>/update/', views.update, name='update'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<int:id>/comment-create', views.comment_create, name='comment_create'),
    path('<int:post_id>/comment-delete/<int:comment_id>', views.comment_delete, name='comment_delete'),
    path('<int:id>/like/', views.like, name='like'),
]
