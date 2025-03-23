from utils import fetch_news, analyze_sentiment, text_to_speech

news = fetch_news("Tesla")
print(news)
print(analyze_sentiment(news[0]["title"]))
print(text_to_speech("यह एक हिंदी भाषा की ऑडियो है।", "hindi_audio.mp3"))