from django.urls import path
from . import views

urlpatterns = [
    path('usersearch/', views.UserSearchList.as_view(), name='usersearch-list'),
    path('usersearch/<int:pk>/', views.UserSearchDetail.as_view(), name='usersearch-detail'),
    
    path('newsarticles/', views.NewsArticlesList.as_view(), name='newsarticles-list'),
    path('newsarticles/<int:pk>/', views.NewsArticlesDetail.as_view(), name='newsarticles-detail'),
    
    path('newsarticlesk1/', views.NewsArticlesK1List.as_view(), name='newsarticlesk1-list'),
    path('newsarticlesk1/<int:pk>/', views.NewsArticlesK1Detail.as_view(), name='newsarticlesk1-detail'),
    
    path('newsarticlesk2/', views.NewsArticlesK2List.as_view(), name='newsarticlesk2-list'),
    path('newsarticlesk2/<int:pk>/', views.NewsArticlesK2Detail.as_view(), name='newsarticlesk2-detail'),
    
    path('newsarticlesk3/', views.NewsArticlesK3List.as_view(), name='newsarticlesk3-list'),
    path('newsarticlesk3/<int:pk>/', views.NewsArticlesK3Detail.as_view(), name='newsarticlesk3-detail'),
    
    path('redditcomments/', views.RedditCommentsList.as_view(), name='redditcomments-list'),
    path('redditcomments/<int:pk>/', views.RedditCommentsDetail.as_view(), name='redditcomments-detail'),
    
    path('redditcommentsk1/', views.RedditCommentsK1List.as_view(), name='redditcommentsk1-list'),
    path('redditcommentsk1/<int:pk>/', views.RedditCommentsK1Detail.as_view(), name='redditcommentsk1-detail'),
    
    path('redditcommentsk2/', views.RedditCommentsK2List.as_view(), name='redditcommentsk2-list'),
    path('redditcommentsk2/<int:pk>/', views.RedditCommentsK2Detail.as_view(), name='redditcommentsk2-detail'),
    
    path('redditcommentsk3/', views.RedditCommentsK3List.as_view(), name='redditcommentsk3-list'),
    path('redditcommentsk3/<int:pk>/', views.RedditCommentsK3Detail.as_view(), name='redditcommentsk3-detail'),

]
