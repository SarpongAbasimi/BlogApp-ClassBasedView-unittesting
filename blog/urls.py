from django.urls import path 
from .views import HomeViewPage,DetailViewPage,BlogCreateView,UpdatePostViewPage,DeletePostViewPage


urlpatterns=[
    path('post/<int:pk>/delete',DeletePostViewPage.as_view(),name='delete_post'),
    path('post/<int:pk>/edit',UpdatePostViewPage.as_view(),name='post_edit'),
    path('post/new/',BlogCreateView.as_view(),name='post_new'),
    path('',HomeViewPage.as_view(),name='home_page'),
    path('post/<int:pk>/',DetailViewPage.as_view(),name='detail_page')

]