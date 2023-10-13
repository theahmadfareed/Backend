from django.shortcuts import render
import requests
from django.http import HttpResponse
from .models import *
import praw
import json
from django.views.decorators.csrf import csrf_exempt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import prawcore
from .serializers import *
from rest_framework import generics

def home(request):
    return HttpResponse("Hello World!")

# @csrf_exempt
# def fetch_data(request):
#     if request.method == 'POST':
#         try:
#             # # Initialize dictionaries to track total response counts
#             total_news_responses = {}
#             total_reddit_responses = {}
#             analyzer = SentimentIntensityAnalyzer() 

#             # Parse the JSON data from the request body
#             data = json.loads(request.body.decode('utf-8'))  # Decode the bytes to a string
#             search_keywords = data.get('keywords', [])
#             user_search = UserSearch(search_terms=search_keywords)
#             user_search.save()

#             total_sentiments = {
#                 "positive_count": 0,
#                 "negative_count": 0,
#                 "neutral_count": 0,
#             }

#             k1_news_data = []
#             k2_news_data = []
#             k3_news_data = []
#             k1_sentiments = {}
#             k2_sentiments = {}
#             k3_sentiments = {}
#             L=[]
            
#             # Define the search keywords
#             api_key = '1a8e8d019bb0420e8aa011b382aa8f76'
#             # Iterate over each search keyword and fetch news articles
#             for index, search_keyword in enumerate(search_keywords):
#                 print("Keyword = " + search_keyword)
#                 url = f'https://newsapi.org/v2/everything?q={search_keyword}&apiKey={api_key}&sort_by=relevancy&language=en&pageSize=100'
#                 response = requests.get(url)

#                 if response.status_code == 200:
#                     # Increment the total news response count
#                     total_news_responses[search_keyword] = len(response.json().get('articles', []))

#                     print(f"News fetched successfully for {search_keyword}!")
#                     data = response.json()
#                     articles = data.get('articles', [])

#                     # Determine the appropriate NewsArticle model based on the index
#                     news_articles_model = None
#                     if index == 0:
#                         news_articles_model = News_Articles_K1
#                     elif index == 1:
#                         news_articles_model = News_Articles_K2
#                     elif index == 2:
#                         news_articles_model = News_Articles_K3
#                     all_news_data = []
#                     # Initialize counters for sentiments
#                     sentiments = {
#                         "keyword": search_keyword,
#                         "positive_count": 0,
#                         "negative_count": 0,
#                         "neutral_count": 0,
#                     }
#                     # Save the news articles to the corresponding model
#                     for article in articles:
#                         author = article.get('author') if article.get('author') else "Unknown"
#                         content = article.get('content')
#                         # Perform sentiment analysis on the article content using VADER
#                         sentiment_scores = analyzer.polarity_scores(content)
#                         compound_score = sentiment_scores['compound']
#                         # Decide sentiment label based on the compound score
#                         if compound_score >= 0.05:
#                             sentiment_label = "Positive"
#                             sentiments['positive_count'] += 1
#                             total_sentiments['positive_count'] += 1
#                         elif compound_score <= -0.05:
#                             sentiment_label = "Negative"
#                             sentiments['negative_count'] += 1
#                             total_sentiments['negative_count'] += 1
#                         else:
#                             sentiment_label = "Neutral"
#                             sentiments['neutral_count'] += 1
#                             total_sentiments['neutral_count'] += 1

#                         data = {"author": author, "content": content, "sentiment": sentiment_label}
#                         all_news_data.append(data)
                        
#                         if index == 0:
#                             k1_news_data = all_news_data
#                             k1_sentiments = sentiments
#                         elif index == 1:
#                             k2_news_data = all_news_data
#                             k2_sentiments = sentiments
#                         elif index == 2:
#                             k3_news_data = all_news_data
#                             k3_sentiments = sentiments
                    
#                     L.append(sentiments)
#                     user_search.each_keyword_sentiments_from_news = L
#                     user_search.save()
                    
#                     news_articles, _ = News_Articles.objects.get_or_create(user_search=user_search)
#                     news_articles.search_terms = search_keywords
#                     news_articles.K1_news_data = k1_news_data
#                     news_articles.K2_news_data = k2_news_data
#                     news_articles.K3_news_data = k3_news_data
#                     news_articles.K1_news_sentiments = k1_sentiments
#                     news_articles.K2_news_sentiments = k2_sentiments
#                     news_articles.K3_news_sentiments = k3_sentiments
#                     news_articles.save()
                    
#                     # data_column = json.dumps(all_data)
#                     news_articles_model.objects.create(
#                         data=all_news_data,
#                         keyword=search_keyword,
#                         sentiments=sentiments,
#                         user_search=user_search
#                     )
#                     print(f"News saved successfully for {search_keyword}!")
#                 # Calculate and update keyword_total_sentiments here
#                 keyword_total_sentiments = {}
#                 for keyword in search_keywords:
#                     keyword_total_sentiments[keyword] = {
#                         "positive_count": 0,
#                         "negative_count": 0,
#                         "neutral_count": 0,
#                     }

#                 for article_model in [News_Articles_K1, News_Articles_K1, News_Articles_K3]:
#                     articles = article_model.objects.filter(user_search=user_search)
#                     for article in articles:
#                         keyword = article.keyword
#                         keyword_total_sentiments[keyword]['positive_count'] += article.sentiments['positive_count']
#                         keyword_total_sentiments[keyword]['negative_count'] += article.sentiments['negative_count']
#                         keyword_total_sentiments[keyword]['neutral_count'] += article.sentiments['neutral_count']


#             # Reddit API credentials
#             client_id = 'VF395KMJmO6y_8kFIEaaxQ'
#             client_secret = 'qYyujCOjm4u7FGmd4gp9pZvYN8eFUw'
#             user_agent = "Django-FYP 1.0 by /u/ahmadfareed"

#             # Initialize the Reddit API client
#             reddit = praw.Reddit(
#                 client_id=client_id,
#                 client_secret=client_secret,
#                 user_agent=user_agent
#             )
#             k1_reddit_data = []
#             k2_reddit_data = []
#             k3_reddit_data = []
#             k1_sentiments = {}
#             k2_sentiments = {}
#             k3_sentiments = {}
#             L=[]
#             # Iterate over each search keyword and fetch related subreddits
#             for index, search_keyword in enumerate(search_keywords):
#                 print("Keyword = " + search_keyword)
#                 formatted_comments = []
#                 # Initialize counters for sentiments
#                 sentiments = {
#                     "keyword": search_keyword,
#                     "positive_count": 0,
#                     "negative_count": 0,
#                     "neutral_count": 0,
#                 }
#                 try:
#                     for comment in reddit.subreddit(search_keyword).comments(limit=100):
#                         print(f"Reddit Comments fetched successfully for {search_keyword}!")
#                         # Extract relevant data from the Redditor object
#                         author_name = comment.author.name if comment.author else "Unknown"
#                         comment_body = comment.body
#                         # Perform sentiment analysis on the comment body using VADER
#                         sentiment_scores = analyzer.polarity_scores(comment_body)
#                         compound_score = sentiment_scores['compound']
#                         # Decide sentiment label based on the compound score
#                         if compound_score >= 0.05:
#                             sentiment_label = "Positive"
#                             sentiments['positive_count'] += 1
#                             total_sentiments['positive_count'] += 1
#                         elif compound_score <= -0.05:
#                             sentiment_label = "Negative"
#                             sentiments['negative_count'] += 1
#                             total_sentiments['negative_count'] += 1
#                         else:
#                             sentiment_label = "Neutral"
#                             sentiments['neutral_count'] += 1
#                             total_sentiments['neutral_count'] += 1

#                         data = {
#                             "author": author_name,
#                             "content": comment_body,
#                             "sentiment": sentiment_label,
#                         }
#                         formatted_comments.append(data)
                        
#                         if index == 0:
#                             k1_reddit_data = formatted_comments
#                             k1_sentiments = sentiments
#                         elif index == 1:
#                             k2_reddit_data = formatted_comments
#                             k2_sentiments = sentiments
#                         elif index == 2:
#                             k3_reddit_data = formatted_comments
#                             k3_sentiments = sentiments
                            
#                     L.append(sentiments)
#                     user_search.each_keyword_sentiments_from_reddit = L
#                     user_search.save()
                    
#                     reddit_comments, _ = Reddit_Comments.objects.get_or_create(user_search=user_search)
#                     reddit_comments.search_terms = search_keywords
#                     reddit_comments.K1_reddit_data = k1_reddit_data
#                     reddit_comments.K2_reddit_data = k2_reddit_data
#                     reddit_comments.K3_reddit_data = k3_reddit_data
#                     reddit_comments.K1_reddit_sentiments = k1_sentiments
#                     reddit_comments.K2_reddit_sentiments = k2_sentiments
#                     reddit_comments.K3_reddit_sentiments = k3_sentiments
#                     reddit_comments.save()
                

#                 except prawcore.exceptions.NotFound:
#                     print(f"Subreddit '{search_keyword}' not found or is private.")
#                     # You can handle this exception as needed, e.g., skip this subreddit
#                     continue
                
#                 # Increment the total Reddit response count
#                 total_reddit_responses[search_keyword] = len(formatted_comments)

#                 # Create an instance of the appropriate model based on the keyword
#                 if index == 0:
#                     reddit_article = Reddit_Comments_K1(sentiments=sentiments, data=formatted_comments,
#                                                     keyword=search_keyword, user_search=user_search)
#                 elif index == 1:
#                     reddit_article = Reddit_Comments_K2(sentiments=sentiments, data=formatted_comments,
#                                                     keyword=search_keyword, user_search=user_search)
#                 elif index == 2:
#                     reddit_article = Reddit_Comments_K3(sentiments=sentiments, data=formatted_comments,
#                                                     keyword=search_keyword, user_search=user_search)
#                 print(f"Reddit Comments saved successfully for {search_keyword}!")
#                 # Calculate and update keyword_total_sentiments here
#                 for article_model in [Reddit_Comments_K1, Reddit_Comments_K2, Reddit_Comments_K3]:
#                     articles = article_model.objects.filter(user_search=user_search)
#                     for article in articles:
#                         keyword = article.keyword
#                         keyword_total_sentiments[keyword]['positive_count'] += article.sentiments['positive_count']
#                         keyword_total_sentiments[keyword]['negative_count'] += article.sentiments['negative_count']
#                         keyword_total_sentiments[keyword]['neutral_count'] += article.sentiments['neutral_count']
#                 user_search.total_sentiments = total_sentiments
#                 user_search.each_keyword_total_sentiments = keyword_total_sentiments
#                 user_search.total_news_responses = total_news_responses
#                 user_search.total_reddit_responses = total_reddit_responses
#                 user_search.save()
#                 # Save the comment to the corresponding model
#                 reddit_article.save()
#             # Return an HTTP response
#             return HttpResponse("Data fetched and saved!")
#         except json.JSONDecodeError:
#             return HttpResponse("Invalid JSON data.", status=400)
#         except Exception as e:
#             # Handle other exceptions here, log them, and return an appropriate response
#             return HttpResponse(f"An error occurred: {str(e)}", status=500)
#     else:
#         return HttpResponse("Invalid request method.", status=405)
    
@csrf_exempt
def fetch_save_data (request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body.decode('utf-8'))  # Decode the bytes to a string
            search_keywords = data.get('keywords', [])
            user_search = UserSearch(search_terms=search_keywords)
            user_search.save()
            
            
            L1 = fetch_save_news_data(search_keywords, user_search)
            L2 = fetch_save_reddit_data(search_keywords, user_search)
            # print("L1 = ",L1)
            # print("L2 = ",L2)
            # Create a dictionary to store the combined sentiment counts
            combined_sentiments = {}

            # Iterate through L1 and update the combined_sentiments dictionary
            for item in L1:
                keyword = item['keyword']
                if keyword not in combined_sentiments:
                    combined_sentiments[keyword] = item
                else:
                    combined_sentiments[keyword]['positive_count'] += item['positive_count']
                    combined_sentiments[keyword]['negative_count'] += item['negative_count']
                    combined_sentiments[keyword]['neutral_count'] += item['neutral_count']

            # Iterate through L2 and update the combined_sentiments dictionary
            for item in L2:
                keyword = item['keyword']
                if keyword not in combined_sentiments:
                    combined_sentiments[keyword] = item
                else:
                    combined_sentiments[keyword]['positive_count'] += item['positive_count']
                    combined_sentiments[keyword]['negative_count'] += item['negative_count']
                    combined_sentiments[keyword]['neutral_count'] += item['neutral_count']
            # Initialize a dictionary to store the total sentiments
            total_sentiments = {'positive': 0, 'negative': 0, 'neutral': 0}

            # Iterate through the combined dictionary and sum sentiment counts
            for counts in combined_sentiments.values():
                total_sentiments['positive'] += counts['positive_count']
                total_sentiments['negative'] += counts['negative_count']
                total_sentiments['neutral'] += counts['neutral_count']

            # Convert the dictionary back to a list
            combined_sentiments_list = list(combined_sentiments.values())
            # print("L3 = ", combined_sentiments_list)
            user_search.each_keyword_total_sentiments = combined_sentiments_list
            user_search.total_sentiments = total_sentiments
            user_search.save()
            
        except Exception as e:
            # Handle other exceptions here, log them, and return an appropriate response
            return HttpResponse(f"An error occurred: {str(e)}", status=500)
    else:
        return HttpResponse("Invalid request method.", status=405)
    
    return HttpResponse("Data fetched and saved successfully.")

@csrf_exempt
def fetch_save_news_data(search_keywords, user_search):
    
    total_news_responses = {}
    
    k1_news_data = []
    k2_news_data = []
    k3_news_data = []
    
    k1_sentiments = {}
    k2_sentiments = {}
    k3_sentiments = {}
    
    L1=[]
    
    api_key = '1a8e8d019bb0420e8aa011b382aa8f76'
    analyzer = SentimentIntensityAnalyzer()
    
    for index, search_keyword in enumerate(search_keywords):
        
        url = f'https://newsapi.org/v2/everything?q={search_keyword}&apiKey={api_key}&sort_by=relevancy&language=en&pageSize=100'
        response = requests.get(url)

        if response.status_code == 200:
            print(f"News fetched successfully for {search_keyword}!")
            
            total_news_responses[search_keyword] = len(response.json().get('articles', []))
            user_search.total_news_responses = total_news_responses
            data = response.json()
            articles = data.get('articles', [])
            
            news_articles_model = None
            if index == 0:
                news_articles_model = News_Articles_K1
            elif index == 1:
                news_articles_model = News_Articles_K2
            elif index == 2:
                news_articles_model = News_Articles_K3
                
            all_news_data = []
            sentiments = {"keyword": search_keyword, "positive_count": 0, "negative_count": 0, "neutral_count": 0}

            for article in articles:
                author = article.get('author') if article.get('author') else "Unknown"
                content = article.get('content')
                sentiment_scores = analyzer.polarity_scores(content)
                compound_score = sentiment_scores['compound']

                if compound_score >= 0.05:
                    sentiment_label = "Positive"
                    sentiments['positive_count'] += 1
                elif compound_score <= -0.05:
                    sentiment_label = "Negative"
                    sentiments['negative_count'] += 1
                else:
                    sentiment_label = "Neutral"
                    sentiments['neutral_count'] += 1

                data = {"author": author, "content": content, "sentiment": sentiment_label}
                all_news_data.append(data)

                if index == 0:
                    k1_news_data = all_news_data
                    k1_sentiments = sentiments
                elif index == 1:
                    k2_news_data = all_news_data
                    k2_sentiments = sentiments
                elif index == 2:
                    k3_news_data = all_news_data
                    k3_sentiments = sentiments
                    
            L1.append(sentiments)
            user_search.each_keyword_sentiments_from_news = L1
            user_search.save()
            
            news_articles, _ = News_Articles.objects.get_or_create(user_search=user_search)
            news_articles.search_terms = search_keywords
            news_articles.K1_news_data = k1_news_data
            news_articles.K2_news_data = k2_news_data
            news_articles.K3_news_data = k3_news_data
            news_articles.K1_news_sentiments = k1_sentiments
            news_articles.K2_news_sentiments = k2_sentiments
            news_articles.K3_news_sentiments = k3_sentiments
            news_articles.save()
            user_search.total_news_responses = total_news_responses
            user_search.save()
            
            news_articles_model.objects.create(
                data=all_news_data,
                keyword=search_keyword,
                sentiments=sentiments,
                user_search=user_search
            )
                        
            print(f"News saved successfully for {search_keyword}!")
            
    return L1

@csrf_exempt
def fetch_save_reddit_data(search_keywords, user_search):
        
    k1_reddit_data = []
    k2_reddit_data = []
    k3_reddit_data = []
    
    k1_sentiments = {}
    k2_sentiments = {}
    k3_sentiments = {}
    
    L2=[]
    
    total_reddit_responses = {}
    analyzer = SentimentIntensityAnalyzer()

    # Reddit API credentials
    client_id = 'VF395KMJmO6y_8kFIEaaxQ'
    client_secret = 'qYyujCOjm4u7FGmd4gp9pZvYN8eFUw'
    user_agent = "Django-FYP 1.0 by /u/ahmadfareed"

    # Initialize the Reddit API client
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent
    )

    for index, search_keyword in enumerate(search_keywords):
        formatted_comments = []
        sentiments = {"keyword": search_keyword, "positive_count": 0, "negative_count": 0, "neutral_count": 0}

        try:
            for comment in reddit.subreddit(search_keyword).comments(limit=100):
                author_name = comment.author.name if comment.author else "Unknown"
                comment_body = comment.body
                sentiment_scores = analyzer.polarity_scores(comment_body)
                compound_score = sentiment_scores['compound']

                if compound_score >= 0.05:
                    sentiment_label = "Positive"
                    sentiments['positive_count'] += 1
                elif compound_score <= -0.05:
                    sentiment_label = "Negative"
                    sentiments['negative_count'] += 1
                else:
                    sentiment_label = "Neutral"
                    sentiments['neutral_count'] += 1

                data = {
                    "author": author_name,
                    "content": comment_body,
                    "sentiment": sentiment_label,
                }
                formatted_comments.append(data)

                if index == 0:
                    k1_reddit_data = formatted_comments
                    k1_sentiments = sentiments
                elif index == 1:
                    k2_reddit_data = formatted_comments
                    k2_sentiments = sentiments
                elif index == 2:
                    k3_reddit_data = formatted_comments
                    k3_sentiments = sentiments
            
            L2.append(sentiments)
            user_search.each_keyword_sentiments_from_reddit = L2
            user_search.save()
                        
            print(f"Reddit Comments fetched successfully for {search_keyword}!")

            reddit_comments, _ = Reddit_Comments.objects.get_or_create(user_search=user_search)
            reddit_comments.search_terms = search_keywords
            reddit_comments.K1_reddit_data = k1_reddit_data
            reddit_comments.K2_reddit_data = k2_reddit_data
            reddit_comments.K3_reddit_data = k3_reddit_data
            reddit_comments.K1_reddit_sentiments = k1_sentiments
            reddit_comments.K2_reddit_sentiments = k2_sentiments
            reddit_comments.K3_reddit_sentiments = k3_sentiments
            reddit_comments.save()
            
        except prawcore.exceptions.NotFound:
            # Handle exceptions for missing or private subreddits
            print(f"Subreddit '{search_keyword}' not found or is private.")
            continue
        
        total_reddit_responses[search_keyword] = len(formatted_comments)
        # Create an instance of the appropriate model based on the keyword
        if index == 0:
            reddit_article = Reddit_Comments_K1(sentiments=sentiments, data=formatted_comments,
                                            keyword=search_keyword, user_search=user_search)
        elif index == 1:
            reddit_article = Reddit_Comments_K2(sentiments=sentiments, data=formatted_comments,
                                            keyword=search_keyword, user_search=user_search)
        elif index == 2:
            reddit_article = Reddit_Comments_K3(sentiments=sentiments, data=formatted_comments,
                                            keyword=search_keyword, user_search=user_search)
        reddit_article.save()
        print(f"Reddit Comments saved successfully for {search_keyword}!")

        user_search.total_reddit_responses = total_reddit_responses
        user_search.save()
    return L2

def display_data(request):
    # Retrieve the data from the models
    user_searches = UserSearch.objects.all()
    news_articles = News_Articles.objects.all()
    reddit_comments = Reddit_Comments.objects.all()
    news_articles_k1 = News_Articles_K1.objects.all()
    news_articles_k2 = News_Articles_K2.objects.all()
    news_articles_k3 = News_Articles_K3.objects.all()
    reddit_comments_k1 = Reddit_Comments_K1.objects.all()
    reddit_comments_k2 = Reddit_Comments_K2.objects.all()
    reddit_comments_k3 = Reddit_Comments_K3.objects.all()

    # You can pass this data to your template as context
    context = {
        'user_searches': user_searches,
        'news_articles': news_articles,
        'reddit_comments': reddit_comments,
        'news_articles_k1': news_articles_k1,
        'news_articles_k2': news_articles_k2,
        'news_articles_k3': news_articles_k3,
        'reddit_comments_k1': reddit_comments_k1,
        'reddit_comments_k2': reddit_comments_k2,
        'reddit_comments_k3': reddit_comments_k3,
    }

    return render(request, 'display_data.html', context)


class UserSearchList(generics.ListCreateAPIView):
    queryset = UserSearch.objects.all()
    serializer_class = UserSearchSerializer

class UserSearchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserSearch.objects.all()
    serializer_class = UserSearchSerializer

class NewsArticlesList(generics.ListCreateAPIView):
    queryset = News_Articles.objects.all()
    serializer_class = NewsArticlesSerializer

class NewsArticlesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = News_Articles.objects.all()
    serializer_class = NewsArticlesSerializer

class NewsArticlesK1List(generics.ListCreateAPIView):
    queryset = News_Articles_K1.objects.all()
    serializer_class = NewsArticlesK1Serializer

class NewsArticlesK1Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = News_Articles_K1.objects.all()
    serializer_class = NewsArticlesK1Serializer

class NewsArticlesK2List(generics.ListCreateAPIView):
    queryset = News_Articles_K2.objects.all()
    serializer_class = NewsArticlesK2Serializer

class NewsArticlesK2Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = News_Articles_K2.objects.all()
    serializer_class = NewsArticlesK2Serializer

class NewsArticlesK3List(generics.ListCreateAPIView):
    queryset = News_Articles_K3.objects.all()
    serializer_class = NewsArticlesK3Serializer

class NewsArticlesK3Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = News_Articles_K3.objects.all()
    serializer_class = NewsArticlesK3Serializer

class RedditCommentsList(generics.ListCreateAPIView):
    queryset = Reddit_Comments.objects.all()
    serializer_class = RedditCommentsSerializer

class RedditCommentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reddit_Comments.objects.all()
    serializer_class = RedditCommentsSerializer

class RedditCommentsK1List(generics.ListCreateAPIView):
    queryset = Reddit_Comments_K1.objects.all()
    serializer_class = RedditCommentsK1Serializer

class RedditCommentsK1Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reddit_Comments_K1.objects.all()
    serializer_class = RedditCommentsK1Serializer

class RedditCommentsK2List(generics.ListCreateAPIView):
    queryset = Reddit_Comments_K2.objects.all()
    serializer_class = RedditCommentsK2Serializer

class RedditCommentsK2Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reddit_Comments_K2.objects.all()
    serializer_class = RedditCommentsK2Serializer

class RedditCommentsK3List(generics.ListCreateAPIView):
    queryset = Reddit_Comments_K3.objects.all()
    serializer_class = RedditCommentsK3Serializer

class RedditCommentsK3Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reddit_Comments_K3.objects.all()
    serializer_class = RedditCommentsK3Serializer