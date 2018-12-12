from django.urls import path 
from .views import HomeViewPage,DetailViewPage


urlpatterns=[
    path('',HomeViewPage.as_view(),name='home_page'),
    path('post/<int:pk>/',DetailViewPage.as_view(),name='detail_page')
]