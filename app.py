
import streamlit as st
import gradio as gr
import asyncio
from utils import extract_news, analyze_sentiment, compare_sentiment, text_to_hindi_speech

st.title("News Sentiment Analysis")

company_name = st.text_input("Enter Company Name:")

if company_name:
    st.subheader(f"News Articles for {company_name}")

    articles_data = extract_news(company_name)

    if articles_data:
        for i, article in enumerate(articles_data):
            st.write(f"### Article {i+1}")
            st.write(f"**Title:** {article['title']}")
            st.write(f"**Summary:** {article['summary']}")

            if "topics" in article and article["topics"]:
                topics_str = ", ".join(article["topics"])
                st.write(f"**Topics:** {topics_str}")

            sentiment = analyze_sentiment(article["summary"])
            article["sentiment"] = sentiment  
            st.write(f"**Sentiment:** {sentiment.capitalize()}")

            st.write(f"[Read Full Article]({article['url']})")
            st.write("---")

        st.subheader("Comparative Sentiment Analysis")
        comparison_results = compare_sentiment(articles_data)
        st.json(comparison_results)

        st.subheader("Hindi Audio Summary")
        report_summary = f"Sentiment analysis report for {company_name}. "
        for article in articles_data:
            report_summary += f"Article: {article['title']}, Sentiment: {article['sentiment']}. "

        audio_file = text_to_hindi_speech(report_summary)

        if audio_file:
            st.audio(audio_file, format="audio/mp3")
        else:
            st.error("Failed to generate audio.")
    else:
        st.warning("No articles found.")
