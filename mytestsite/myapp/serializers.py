from rest_framework import serializers
from .models import *

class UserSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSearch
        fields = '__all__'

class NewsArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = News_Articles
        fields = '__all__'

class NewsArticlesK1Serializer(serializers.ModelSerializer):
    class Meta:
        model = News_Articles_K1
        fields = '__all__'

class NewsArticlesK2Serializer(serializers.ModelSerializer):
    class Meta:
        model = News_Articles_K2
        fields = '__all__'

class NewsArticlesK3Serializer(serializers.ModelSerializer):
    class Meta:
        model = News_Articles_K3
        fields = '__all__'

class RedditCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reddit_Comments
        fields = '__all__'

class RedditCommentsK1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Reddit_Comments_K1
        fields = '__all__'

class RedditCommentsK2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Reddit_Comments_K2
        fields = '__all__'

class RedditCommentsK3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Reddit_Comments_K3
        fields = '__all__'
