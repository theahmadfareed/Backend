# Create your models here.
from django.db import models

class UserSearch(models.Model):
    search_terms = models.TextField(null=True)
    created_at =  models.DateField(auto_now_add=True)
    each_keyword_total_news_responses = models.TextField(null=True)
    each_keyword_total_reddit_responses = models.TextField(null=True)
    total_sentiments = models.JSONField(default=None,null=True)
    each_keyword_sentiments_from_news = models.JSONField(default=None,null=True)
    each_keyword_sentiments_from_reddit = models.JSONField(default=None,null=True)
    each_keyword_combine_data = models.JSONField(default=None,null=True)
    each_keyword_total_sentiments = models.JSONField(default=None,null=True)
    graph_data = models.JSONField(default=None,null=True)

class News_Articles(models.Model):
    user_search = models.ForeignKey(UserSearch, on_delete=models.CASCADE)
    search_terms = models.TextField(null=True)
    K1_news_data = models.JSONField(default=None,null=True)
    K1_news_sentiments = models.JSONField(default=None,null=True)
    K2_news_data = models.JSONField(default=None,null=True)
    K2_news_sentiments = models.JSONField(default=None,null=True)
    K3_news_data = models.JSONField(default=None,null=True)
    K3_news_sentiments = models.JSONField(default=None,null=True)
    each_keyword_combine_data = models.JSONField(default=None,null=True)
    each_keyword_total_sentiments = models.JSONField(default=None,null=True)
class News_Articles_K1(models.Model):
    user_search = models.ForeignKey(UserSearch, on_delete=models.CASCADE)
    data = models.JSONField(default=list)
    sentiments = models.JSONField(default=None,null=True)
class News_Articles_K2(models.Model):
    user_search = models.ForeignKey(UserSearch, on_delete=models.CASCADE)
    data = models.JSONField(default=list)
    sentiments = models.JSONField(default=None,null=True)
class News_Articles_K3(models.Model):
    user_search = models.ForeignKey(UserSearch, on_delete=models.CASCADE)
    data = models.JSONField(default=list)
    sentiments = models.JSONField(default=None,null=True)
    
    
class Reddit_Comments(models.Model):
    user_search = models.ForeignKey(UserSearch, on_delete=models.CASCADE)
    search_terms = models.TextField(null=True)
    K1_reddit_data = models.JSONField(default=None,null=True)
    K1_reddit_sentiments = models.JSONField(default=None,null=True)
    K2_reddit_data = models.JSONField(default=None,null=True)
    K2_reddit_sentiments = models.JSONField(default=None,null=True)
    K3_reddit_data = models.JSONField(default=None,null=True)
    K3_reddit_sentiments = models.JSONField(default=None,null=True)
    each_keyword_combine_data = models.JSONField(default=None,null=True)
    each_keyword_total_sentiments = models.JSONField(default=None,null=True)
class Reddit_Comments_K1(models.Model):
    user_search = models.ForeignKey(UserSearch, on_delete=models.CASCADE)
    data = models.JSONField(default=list)
    sentiments = models.JSONField(default=None,null=True)
class Reddit_Comments_K2(models.Model):
    user_search = models.ForeignKey(UserSearch, on_delete=models.CASCADE)
    data = models.JSONField(default=list)
    sentiments = models.JSONField(default=None,null=True)
class Reddit_Comments_K3(models.Model):
    user_search = models.ForeignKey(UserSearch, on_delete=models.CASCADE)    
    data = models.JSONField(default=list)
    sentiments = models.JSONField(default=None,null=True)
    





