from datetime import datetime
from django.shortcuts import render
import requests
from django.http import HttpResponse, JsonResponse
from .models import *
import praw
import json
from django.views.decorators.csrf import csrf_exempt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import prawcore
from .serializers import *
from rest_framework import generics
import pytz
from collections import defaultdict

@csrf_exempt
def signUp(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))  # Decode the bytes to a string
        name = data.get('u_name', '')  # Get the 'u_name' from POST data
        email = data.get('u_email', '')  # Get the 'u_email' from POST data

        if name and email:  # Check if name and email are not empty
            user_profile = UserProfile(u_name=name, u_email=email)
            user_profile.save()
            return JsonResponse({"message": "Record Saved!"})
        else:
            return JsonResponse({"error": "Name and email are required fields."}, status=400)
    else:
        return JsonResponse({"error": "Invalid request method."}, status=405)

@csrf_exempt
def signIn(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))  # Decode the bytes to a string
        name = data.get('u_name', '')  # Get the 'u_name' from POST data
        print(name)
        user_profile = UserProfile.objects.get(u_name=name)
        # If the user is found, return their email in the response
        response_data = {'message': 'User exists', 'email': user_profile.u_email}
        return JsonResponse(response_data)
    else:
        return HttpResponse("Invalid", status=400)  # Return a 400 Bad Request response for other request methods

@csrf_exempt
def fetch_save_data (request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body.decode('utf-8'))  # Decode the bytes to a string
            search_keywords = data.get('keywords', [])
            user_search = UserSearch(search_terms=search_keywords)
            user_search.save()
                        
            each_keyword_sentiments_from_reddit, each_keyword_reddit_combine_data = fetch_save_reddit_data(search_keywords, user_search)
            each_keyword_sentiments_from_news, each_keyword_news_combine_data = fetch_save_news_data(search_keywords, user_search)
            
            combined_data = []
            combined_data.extend(each_keyword_news_combine_data)
            combined_data.extend(each_keyword_reddit_combine_data)
            sorted_data = sorted(combined_data, key=lambda x: x['data']['published_at'], reverse=True)
            
            user_search.each_keyword_combine_data = sorted_data
            user_search.save()

            # Initialize dictionaries to store sentiment counts
            sentiment_counts = defaultdict(lambda: defaultdict(int))

            # Iterate through the sorted_data and count sentiments for each date
            for data in sorted_data:
                date = data["data"]["published_at"][:10]  # Extract the date
                sentiment = data["data"]["sentiment_label"]
                sentiment_counts[date][sentiment] += 1

            # Create the final lists
            dates = sorted(sentiment_counts.keys())
            positive = [sentiment_counts[date]["Positive"] for date in dates]
            negative = [sentiment_counts[date]["Negative"] for date in dates]
            neutral = [sentiment_counts[date]["Neutral"] for date in dates]
            result_data = {
                "Dates":dates,
                "Positive":positive,
                "Negative":negative,
                "Neutral":neutral,
            }
            user_search.graph_data = result_data
            user_search.save()

            # Initialize an empty L3
            each_key_sentiment = []

            # Iterate through keywords in L1 and L2
            for keyword_data1, keyword_data2 in zip(each_keyword_sentiments_from_news, each_keyword_sentiments_from_reddit):
                # Ensure the keywords match
                assert keyword_data1["keyword"] == keyword_data2["keyword"]
                keyword = keyword_data1["keyword"]

                # Calculate the total sentiments for the keyword
                L3 = {
                    "keyword": keyword,
                    "neutral_count": keyword_data1["neutral_count"] + keyword_data2["neutral_count"],
                    "negative_count": keyword_data1["negative_count"] + keyword_data2["negative_count"],
                    "positive_count": keyword_data1["positive_count"] + keyword_data2["positive_count"],
                }

                each_key_sentiment.append(L3)
                
            user_search.each_keyword_total_sentiments = each_key_sentiment
            user_search.save()

            ls=[]
            total_sentiments = {
                "total_positive": 0,
                "total_negative": 0,
                "total_neutral": 0
            }

            for keyword_data in each_key_sentiment:
                total_sentiments["total_positive"] += keyword_data["positive_count"]
                total_sentiments["total_negative"] += keyword_data["negative_count"]
                total_sentiments["total_neutral"] += keyword_data["neutral_count"]
            ls.append(total_sentiments)    
            user_search.total_sentiments = ls
            user_search.save()
            
            return JsonResponse({"project_id": user_search.id, "message": "Data fetched and saved successfully."}, status=200)

        except Exception as e:
            # Handle other exceptions here, log them, and return an appropriate response
            return HttpResponse(f"An error occurred: {str(e)}", status=500)
    else:
        return HttpResponse("Invalid request method.", status=405)
    
@csrf_exempt
def fetch_save_news_data(search_keywords, user_search):
    
    each_keyword_total_news_responses = {}
    each_keyword_sentiments_from_news=[]
    
    k1_news_data = []
    k2_news_data = []
    k3_news_data = []
    
    k1_sentiments = {}
    k2_sentiments = {}
    k3_sentiments = {}
    
    
    api_key = '1a8e8d019bb0420e8aa011b382aa8f76'
    analyzer = SentimentIntensityAnalyzer()
    
    for index, search_keyword in enumerate(search_keywords):
        
        url = f'https://newsapi.org/v2/everything?q=+{search_keyword}&apiKey={api_key}&sort_by=relevancy&language=en&pageSize=100'
        response = requests.get(url)

        if response.status_code == 200:
            print(f"News Articles fetched successfully for {search_keyword}!")
            
            each_keyword_total_news_responses[search_keyword] = len(response.json().get('articles', []))
            user_search.each_keyword_total_news_responses = each_keyword_total_news_responses
            user_search.save()
            
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
                
                source_name = "News"
                author = article.get('author') if article.get('author') else "Unknown"
                content = article.get('description') if article.get('description') else "Unknown"

                published_at_str = article.get('publishedAt')
                if published_at_str.endswith('Z'):
                    published_at_str = published_at_str[:-1]
                published_at_datetime = datetime.strptime(published_at_str, "%Y-%m-%dT%H:%M:%S")
                formatted_published_at = published_at_datetime.strftime("%Y-%m-%d %H:%M:%S")

                url_to_image = "https://newsapi.org/images/n-logo-border.png"
                url = article.get('url') if article.get('url') else "Unknown"
                title = article.get('title') if article.get('title') else "Unknown"
                sentiment_label = analyze_sentiment(analyzer, content, sentiments)

                data = {
                    "keyword":search_keyword,
                    'data':{
                        "source_name":source_name,
                        "author": author,
                        "content": content,
                        "sentiment_label": sentiment_label,
                        "published_at":formatted_published_at,
                        "url":url,
                        "url_to_image":url_to_image,
                        "title":title
                        }
                    }
                all_news_data.append(data)

                if index == 0:
                    k1_news_data = all_news_data
                    k1_sentiments = sentiments
                    # Initialize dictionaries to store sentiment counts
                    sentiment_counts_k1 = defaultdict(lambda: defaultdict(int))
                    # Iterate through the sorted_data and count sentiments for each date
                    for data in k1_news_data:
                        date = data["data"]["published_at"][:10]  # Extract the date
                        sentiment = data["data"]["sentiment_label"]
                        sentiment_counts_k1[date][sentiment] += 1
                    # Create the final lists
                    k1_dates = sorted(sentiment_counts_k1.keys())
                    k1_positive = [sentiment_counts_k1[date]["Positive"] for date in k1_dates]
                    k1_negative = [sentiment_counts_k1[date]["Negative"] for date in k1_dates]
                    k1_neutral = [sentiment_counts_k1[date]["Neutral"] for date in k1_dates]
                    k1_graph_data = {
                        "Keyword":search_keyword,
                        "Dates":k1_dates,
                        "Positive":k1_positive,
                        "Negative":k1_negative,
                        "Neutral":k1_neutral,
                    }
                    user_search.k1_news_graph_data = k1_graph_data
                    user_search.save()
                elif index == 1:
                    k2_news_data = all_news_data
                    k2_sentiments = sentiments
                    # Initialize dictionaries to store sentiment counts
                    sentiment_counts_k2 = defaultdict(lambda: defaultdict(int))
                    # Iterate through the sorted_data and count sentiments for each date
                    for data in k2_news_data:
                        date = data["data"]["published_at"][:10]  # Extract the date
                        sentiment = data["data"]["sentiment_label"]
                        sentiment_counts_k2[date][sentiment] += 1
                    # Create the final lists
                    k2_dates = sorted(sentiment_counts_k2.keys())
                    k2_positive = [sentiment_counts_k2[date]["Positive"] for date in k2_dates]
                    k2_negative = [sentiment_counts_k2[date]["Negative"] for date in k2_dates]
                    k2_neutral = [sentiment_counts_k2[date]["Neutral"] for date in k2_dates]
                    k2_graph_data = {
                        "Keyword":search_keyword,
                        "Dates":k2_dates,
                        "Positive":k2_positive,
                        "Negative":k2_negative,
                        "Neutral":k2_neutral,
                    }
                    user_search.k2_news_graph_data = k2_graph_data
                    user_search.save()
                    
                elif index == 2:
                    k3_news_data = all_news_data
                    k3_sentiments = sentiments
                    # Initialize dictionaries to store sentiment counts
                    sentiment_counts_k3 = defaultdict(lambda: defaultdict(int))
                    # Iterate through the sorted_data and count sentiments for each date
                    for data in k3_news_data:
                        date = data["data"]["published_at"][:10]  # Extract the date
                        sentiment = data["data"]["sentiment_label"]
                        sentiment_counts_k3[date][sentiment] += 1
                    # Create the final lists
                    k3_dates = sorted(sentiment_counts_k3.keys())
                    k3_positive = [sentiment_counts_k3[date]["Positive"] for date in k3_dates]
                    k3_negative = [sentiment_counts_k3[date]["Negative"] for date in k3_dates]
                    k3_neutral = [sentiment_counts_k3[date]["Neutral"] for date in k3_dates]
                    k3_graph_data = {
                        "Keyword":search_keyword,
                        "Dates":k3_dates,
                        "Positive":k3_positive,
                        "Negative":k3_negative,
                        "Neutral":k3_neutral,
                    }
                    user_search.k3_news_graph_data = k3_graph_data
                    user_search.save()
            each_keyword_sentiments_from_news.append(sentiments)
            user_search.each_keyword_sentiments_from_news = each_keyword_sentiments_from_news
            user_search.save()
            #
            each_keyword_news_combine_data = []
            each_keyword_news_combine_data.extend(k1_news_data)
            each_keyword_news_combine_data.extend(k2_news_data)
            each_keyword_news_combine_data.extend(k3_news_data)
            
            news_articles, _ = News_Articles.objects.get_or_create(user_search=user_search)
            news_articles.search_terms = search_keywords
            news_articles.K1_news_data = k1_news_data
            news_articles.K2_news_data = k2_news_data
            news_articles.K3_news_data = k3_news_data
            news_articles.K1_news_sentiments = k1_sentiments
            news_articles.K2_news_sentiments = k2_sentiments
            news_articles.K3_news_sentiments = k3_sentiments
            news_articles.each_keyword_combine_data = each_keyword_news_combine_data #l1
            news_articles.each_keyword_total_sentiments = each_keyword_sentiments_from_news #L1
            news_articles.save()
            
            news_articles_model.objects.create(
                data=all_news_data,
                sentiments=sentiments,
                user_search=user_search
            )
        
            print(f"News Articles saved successfully for {search_keyword}!")
            
    return each_keyword_sentiments_from_news, each_keyword_news_combine_data

@csrf_exempt
def fetch_save_reddit_data(search_keywords, user_search):
        
    each_keyword_total_reddit_responses = {}
    each_keyword_sentiments_from_reddit=[]
    
    k1_reddit_data = []
    k2_reddit_data = []
    k3_reddit_data = []
    
    k1_sentiments = {}
    k2_sentiments = {}
    k3_sentiments = {}
    
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
    # if hasattr(reddit, "search"):
    #     print("The search() method is available on the Reddit object.")
    # else:
    #     print("The search() method is not available on the Reddit object.")
        
    for index, search_keyword in enumerate(search_keywords):
        sentiments = {"keyword": search_keyword, "positive_count": 0, "negative_count": 0, "neutral_count": 0}

        formatted_comments = []
        try:
            
            subreddit = reddit.subreddit(search_keyword)
            for submission in subreddit.hot(limit=100):
                title = submission.title
                source_name = "Reddit"
                url = submission.url
                author = submission.author.name if submission.author else "Unknown"
                content = submission.selftext
                published_at = str(datetime.fromtimestamp(submission.created_utc))
                url_to_image = "https://cdn-icons-png.flaticon.com/512/2111/2111589.png"
                sentiment_label = analyze_sentiment(analyzer, content, sentiments)
                
                data = {
                    'keyword':search_keyword,
                    'data':{
                    'title':title,
                    'source_name':source_name,
                    'url':url,
                    'author':author,
                    'content':content,
                    'published_at':published_at,
                    'sentiment_label':sentiment_label,
                    'url_to_image':url_to_image,
                    }
                }
                formatted_comments.append(data)
                
            if index == 0:
                k1_reddit_data = formatted_comments
                k1_sentiments = sentiments
                # Initialize dictionaries to store sentiment counts
                sentiment_counts_k1 = defaultdict(lambda: defaultdict(int))
                # Iterate through the sorted_data and count sentiments for each date
                for data in k1_reddit_data:
                    date = data["data"]["published_at"][:10]  # Extract the date
                    sentiment = data["data"]["sentiment_label"]
                    sentiment_counts_k1[date][sentiment] += 1
                # Create the final lists
                k1_dates = sorted(sentiment_counts_k1.keys())
                k1_positive = [sentiment_counts_k1[date]["Positive"] for date in k1_dates]
                k1_negative = [sentiment_counts_k1[date]["Negative"] for date in k1_dates]
                k1_neutral = [sentiment_counts_k1[date]["Neutral"] for date in k1_dates]
                k1_graph_data = {
                    "Keyword":search_keyword,
                    "Dates":k1_dates,
                    "Positive":k1_positive,
                    "Negative":k1_negative,
                    "Neutral":k1_neutral,
                }
                user_search.k1_reddit_graph_data = k1_graph_data
                user_search.save()
            elif index == 1:
                k2_reddit_data = formatted_comments
                k2_sentiments = sentiments
                # Initialize dictionaries to store sentiment counts
                sentiment_counts_k2 = defaultdict(lambda: defaultdict(int))
                # Iterate through the sorted_data and count sentiments for each date
                for data in k2_reddit_data:
                    date = data["data"]["published_at"][:10]  # Extract the date
                    sentiment = data["data"]["sentiment_label"]
                    sentiment_counts_k2[date][sentiment] += 1
                # Create the final lists
                k2_dates = sorted(sentiment_counts_k2.keys())
                k2_positive = [sentiment_counts_k2[date]["Positive"] for date in k2_dates]
                k2_negative = [sentiment_counts_k2[date]["Negative"] for date in k2_dates]
                k2_neutral = [sentiment_counts_k2[date]["Neutral"] for date in k2_dates]
                k2_graph_data = {
                    "Keyword":search_keyword,
                    "Dates":k2_dates,
                    "Positive":k2_positive,
                    "Negative":k2_negative,
                    "Neutral":k2_neutral,
                }
                user_search.k2_reddit_graph_data = k2_graph_data
                user_search.save()
            elif index == 2:
                k3_reddit_data = formatted_comments
                k3_sentiments = sentiments
                # Initialize dictionaries to store sentiment counts
                sentiment_counts_k3 = defaultdict(lambda: defaultdict(int))
                # Iterate through the sorted_data and count sentiments for each date
                for data in k3_reddit_data:
                    date = data["data"]["published_at"][:10]  # Extract the date
                    sentiment = data["data"]["sentiment_label"]
                    sentiment_counts_k3[date][sentiment] += 1
                # Create the final lists
                k3_dates = sorted(sentiment_counts_k3.keys())
                k3_positive = [sentiment_counts_k3[date]["Positive"] for date in k3_dates]
                k3_negative = [sentiment_counts_k3[date]["Negative"] for date in k3_dates]
                k3_neutral = [sentiment_counts_k3[date]["Neutral"] for date in k3_dates]
                k3_graph_data = {
                    "Keyword":search_keyword,
                    "Dates":k3_dates,
                    "Positive":k3_positive,
                    "Negative":k3_negative,
                    "Neutral":k3_neutral,
                }
                user_search.k3_reddit_graph_data = k3_graph_data
                user_search.save()
                
            each_keyword_sentiments_from_reddit.append(sentiments)
            user_search.each_keyword_sentiments_from_reddit = each_keyword_sentiments_from_reddit
            user_search.save()
            #
            each_keyword_reddit_combine_data = []
            each_keyword_reddit_combine_data.extend(k1_reddit_data)
            each_keyword_reddit_combine_data.extend(k2_reddit_data)
            each_keyword_reddit_combine_data.extend(k3_reddit_data)

            print(f"Reddit Posts fetched successfully for {search_keyword}!")

            reddit_comments, _ = Reddit_Comments.objects.get_or_create(user_search=user_search)
            reddit_comments.search_terms = search_keywords
            reddit_comments.K1_reddit_data = k1_reddit_data
            reddit_comments.K2_reddit_data = k2_reddit_data
            reddit_comments.K3_reddit_data = k3_reddit_data
            reddit_comments.K1_reddit_sentiments = k1_sentiments
            reddit_comments.K2_reddit_sentiments = k2_sentiments
            reddit_comments.K3_reddit_sentiments = k3_sentiments
            reddit_comments.each_keyword_combine_data = each_keyword_reddit_combine_data #l2
            reddit_comments.each_keyword_total_sentiments = each_keyword_sentiments_from_reddit #l2
            reddit_comments.save()

        except prawcore.exceptions.NotFound:
            # Handle exceptions for missing or private subreddits
            print(f"Subreddit '{search_keyword}' not found or is private.")
            continue

        each_keyword_total_reddit_responses[search_keyword] = len(formatted_comments)
        user_search.each_keyword_total_reddit_responses = each_keyword_total_reddit_responses
        user_search.save()
        # Create an instance of the appropriate model based on the keyword
        if index == 0:
            reddit_article = Reddit_Comments_K1(sentiments=sentiments, data=formatted_comments, user_search=user_search)
        elif index == 1:
            reddit_article = Reddit_Comments_K2(sentiments=sentiments, data=formatted_comments, user_search=user_search)
        elif index == 2:
            reddit_article = Reddit_Comments_K3(sentiments=sentiments, data=formatted_comments, user_search=user_search)
        reddit_article.save()
        print(f"Reddit Posts saved successfully for {search_keyword}!")

    return each_keyword_sentiments_from_reddit, each_keyword_reddit_combine_data

@csrf_exempt
def analyze_sentiment(analyzer, comment_body, sentiments):
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

    return sentiment_label

@csrf_exempt
def display_data(request):
    # Retrieve the data from the models
    user_searches = UserSearch.objects.all()
    # You can pass this data to your template as context
    context = {
        'user_searches': user_searches,
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