from django.urls import path
from . import views


urlpatterns = [
    # ex: members/
    path('', views.index, name='index'),
    # ex: members/demo/
    path('demo/', views.demo, name='demo'),
    # ex: members/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: memebers/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: members/5/vote/
    path('<int:question_id>/cote/', views.vote, name='vote'),
    # ex: members/post/
    path('post/', views.BlogListView.as_view(), name='home'),
    # ex: members/detail/
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
    # ex: members/new/
    path('post/new/', views.BlogCreateView.as_view(), name='new_post'),
    # ex:members/5/edit
    path('post/<int:pk>/edit', views.BlogUpdateView.as_view(), name='post_edit'),
    # ex: members/5/delete
    path('post/<int:pk>/delete', views.BlogDeleteView.as_view(), name='post_delete')

]
