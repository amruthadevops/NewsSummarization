import requests
import random
import time
import os
from bs4 import BeautifulSoup
from transformers import pipeline
from gtts import gTTS
from keybert import KeyBERT  


kw_model = KeyBERT()

#  List of User-Agents to avoid getting blocked
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36"
]

#  1. Extract News Articles
def extract_news(company_name):
    
    search_query = f"{company_name} news"
    search_url = f"https://www.bing.com/news/search?q={search_query}"  
    
    headers = {"User-Agent": random.choice(USER_AGENTS)}

    response = get_with_retries(search_url, headers)
    if not response:
        return [] 

    soup = BeautifulSoup(response.content, "html.parser")
    article_links = []

    for link in soup.find_all("a", href=True):
        href = link["href"]
        if "http" in href and href not in article_links:
            article_links.append(href)

    articles_data = []
    
    for url in article_links[:10]:  
        try:
            article_response = get_with_retries(url, headers)
            if not article_response:
                continue

            article_soup = BeautifulSoup(article_response.content, "html.parser")
            title = article_soup.find("h1").text if article_soup.find("h1") else "No Title Found"
            summary = article_soup.find("p").text if article_soup.find("p") else "No Summary Found"
            topics = extract_key_topics(summary)

            articles_data.append({
                "title": title,
                "summary": summary,
                "topics": topics,  
                "url": url
            })
        except Exception as e:
            print(f"Error processing {url}: {e}")

    return articles_data

#  2. Extract Key Topics
def extract_key_topics(text):
    try:
        topics = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words="english", top_n=5)
        return [topic[0] for topic in topics]  
    except Exception as e:
        print(f"Error extracting topics: {e}")
        return []

#  3. Sentiment Analysis
sentiment_analyzer = pipeline(
    "sentiment-analysis", 
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

def analyze_sentiment(text):
    
    try:
        truncated_text = " ".join(text.split()[:500])  
        result = sentiment_analyzer(truncated_text)[0]
        return result["label"].lower()
    except Exception as e:
        print(f"Sentiment analysis error: {e}")
        return "neutral"

#  4. Comparative Sentiment Analysis
def compare_sentiment(articles_data):
    
    sentiment_counts = {"positive": 0, "negative": 0, "neutral": 0}
    comparisons = []

    for article in articles_data:
        article["sentiment"] = analyze_sentiment(article["summary"])
        sentiment_counts[article["sentiment"]] += 1

    for i in range(len(articles_data)):
        for j in range(i + 1, len(articles_data)):
            comparisons.append({
                "Comparison": f"Article {i+1} ({articles_data[i]['sentiment']}) vs. Article {j+1} ({articles_data[j]['sentiment']})",
                "Impact": "Varies depending on context (e.g., positive vs. negative impacts)."
            })

    return {
        "Sentiment Distribution": sentiment_counts,
        "Coverage Differences": comparisons
    }

#  5. Convert Text to Hindi Speech
def text_to_hindi_speech(text, filename="hindi_audio.mp3"):
    try:
        if not os.path.exists("static"):
            os.makedirs("static")

        filepath = f"static/{filename}"

        # Translate English text to Hindi using `deep-translator`
        from deep_translator import GoogleTranslator
        hindi_text = GoogleTranslator(source="en", target="hi").translate(text)

        # Generate Hindi speech
        hindi_tts = gTTS(text=hindi_text, lang="hi", slow=False)
        hindi_tts.save(filepath)

        return filepath
    except Exception as e:
        print(f"Error generating TTS: {e}")
        return "static/fallback.mp3" 
    
    
from collections import Counter

def compare_sentiment(articles_data):
    """
    Compares sentiment across the articles.

    Args:
        articles_data (list): List of article dictionaries.

    Returns:
        dict: Sentiment distribution, most common topics, and coverage differences.
    """
    sentiment_counts = Counter()
    topic_counts = Counter()
    comparisons = []

    for article in articles_data:
        sentiment_counts[article["sentiment"]] += 1
        topic_counts.update(article["topics"])

    # Generate comparisons between articles
    for i in range(len(articles_data)):
        for j in range(i + 1, len(articles_data)):
            comparisons.append({
                "Comparison": f"Article {i+1} ({articles_data[i]['sentiment']}) vs. Article {j+1} ({articles_data[j]['sentiment']})",
                "Impact": "Varies depending on context (e.g., positive vs. negative impacts)."
            })

    return {
        "Sentiment Distribution": dict(sentiment_counts),
        "Most Frequent Topics": topic_counts.most_common(5),  # Top 5 topics
        "Coverage Differences": comparisons
    }
 

#  6. GET Request with Automatic Retries
def get_with_retries(url, headers, retries=3, delay=5):

    for i in range(retries):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            if i < retries - 1:
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)
    return None  

