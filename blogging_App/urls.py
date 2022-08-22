from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('addpost/', views.addpost.as_view(), name='addpost'),
    path('<slug:slug>/update/', views.updatepost.as_view(), name='updatepost'),
    path('<slug:slug>/delete/', views.deletepost.as_view(), name='delete'),
    path('blog/', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail, name='post_detail'),
    path('support/', views.support, name='support'),
    

]
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),