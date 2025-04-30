
# 📰 News Sentiment Analysis with  Text-to-Speech

## 📌 Overview

Analyze real-time company news, extract sentiment and key topics, and generate Hindi audio summaries using cutting-edge NLP and TTS technologies.


This project fetches the latest news articles about a given company, performs sentiment analysis, extracts key topics, and generates a Hindi spoken summary using Text-to-Speech (TTS). It includes a REST API built with Flask and a user-friendly Streamlit UI.

## Features

🔍 Real-Time News Scraping from multiple online sources.

💬 Sentiment Analysis using pre-trained transformer models (Hugging Face).

📌 Key Topic Extraction with KeyBERT.

🗣️ Hindi Audio Summarization with Google Text-to-Speech (gTTS).

🌐 RESTful API for programmatic access.

🖥️ Streamlit Web App for interactive use.

🌍 Multilingual Support for broader accessibility.

🔓 Open-source and free — no paid API dependencies.
## Tech Stack


Backend API:	    Flask (Python)

Frontend:   	    Streamlit

Scraping:   	    Requests, BeautifulSoup4

Sentiment Model:    Transformers (BERT-like)

Topic Extraction:	KeyBERT

Text-to-Speech: 	gTTS (Google Text-to-Speech)

Deployment Ready: 	Flask API & Streamlit (local/cloud)

#### 1. Clone the Repository

```bash
git clone https://github.com/amruthadevops/NewsSummarization
cd NewsSummarization
```
#### 2. Create a Virtual Environment
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```
#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```




## Running the Application

#### 1. Start the Flask API
```bash
python app.py
```

#### 2. Start the Streamlit UI
```bash
streamlit run app.py
```

##  API Usage

#### Endpoint: /news_report (POST)
Request Payload:
```bash
json
{
  "company_name": "Tesla"
}
```
Example CURL:
```bash
curl -X POST -H "Content-Type: application/json" \ -d '{"company_name": "Tesla"}' \http://localhost:5000/news_report
```
Response:
```json
{
  "summary": "Tesla stock surges amid strong quarterly results...",
  "sentiment": "Positive",
  "topics": ["electric vehicles", "earnings", "Elon Musk"]
}
```


## 🧪 Model Details
Sentiment Analysis: Transformer models fine-tuned on financial/news datasets.

Topic Extraction: KeyBERT leverages BERT embeddings for keyword generation.

Hindi TTS: gTTS supports Hindi conversion and playback of summary text.

## ⚠️ Assumptions & Limitations
Website structure changes may break web scraping.

Sentiment analysis may misclassify sarcasm or mixed sentiments.

TTS output is limited to gTTS’s pronunciation capabilities.

Currently optimized for Hindi language; support for others is experimental.

No rate limiting or authentication yet — not production-hardened.

## 🔄 Future Improvements
📰 Add more diverse and resilient news sources.

🧠 Train or fine-tune sentiment models on financial news.

🌐 Add support for other languages (e.g., Tamil, Bengali, English).

🎙️ Integrate advanced Hindi TTS like Coqui or NVIDIA FastSpeech.

☁️ Deploy on AWS/GCP with public endpoints and authentication.
## Authors

- [@Amrutha](https://github.com/amruthadevops?tab=overview&from=2025-02-01&to=2025-02-28)

- [@LinkedIn ](https://www.linkedin.com/in/amrutha-c-4a2362280/?trk=opento_sprofile_details)

## License

[MIT](https://choosealicense.com/licenses/mit/)

This project is licensed under the MIT License — feel free to use, contribute, and share!
