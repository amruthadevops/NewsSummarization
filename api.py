from flask import Flask, request, jsonify  
from utils import extract_news, analyze_sentiment, compare_sentiment, text_to_hindi_speech

app = Flask(__name__)

@app.route("/news_report", methods=["POST"])
def get_news_report():

    data = request.get_json()

    if not data or "company_name" not in data:
        return jsonify({"error": "Company name is required"}), 400  

    company_name = data["company_name"]

    articles_data = extract_news(company_name)

    if articles_data:
        for article in articles_data:
            article["sentiment"] = analyze_sentiment(article["summary"])

        comparison_results = compare_sentiment(articles_data)

        report_summary = f"Sentiment analysis report for {company_name}. "
        for article in articles_data:
            report_summary += f"Article: {article['title']}, Sentiment: {article['sentiment']}. "

        audio_file = text_to_hindi_speech(report_summary)

        response = {
            "company": company_name,
            "articles": articles_data,
            "comparative_analysis": comparison_results,
            "audio_file": audio_file  
        }
        return jsonify(response), 200
    else:
        return jsonify({"message": "No articles found"}), 200

if __name__ == "__main__":
    app.run(debug=True)
