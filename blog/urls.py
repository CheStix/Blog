from django.urls import path
from .views import post_list, post_detail, PostListView, post_share

app_name = 'blog'

urlpatterns = [
    # post views
    path('', post_list, name='post_list_url'),
    # path('', PostListView.as_view(), name='post_list_url'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail_url'),
    path('<int:post_id>/share/', post_share, name='post_share_url'),
    path('tag/<slug:tag_slug>/', post_list, name='post_list_by_tag_url'),
]