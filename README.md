# News Sentiment Analysis

#  Overview
This project fetches the latest news articles about a company, analyzes the sentiment, extracts key topics, and generates a Hindi text-to-speech summary.

## Features
1. Enhance web scraping with multiple sources to avoid reliance on a single website.
2. Improve sentiment accuracy by using fine-tuned transformers on financial/news datasets.
3. Add multilingual support for sentiment analysis and topic extraction.
4. Implement a more advanced Hindi TTS model for improved pronunciation.
5. Deploy API and Streamlit UI online for public access.

### Project Setup

1 Clone the Repository
    ```sh
    git clone https://github.com/your-username/your-repository.git
    cd your-repository ```
2.Create a Virtual Environment
    # Windows (PowerShell)
     python -m venv venv
     venv\Scripts\activate
3.Install Dependencies
    pip install -r requirements.txt
4.Running the Application
    1.Start the Flask API
        python app.py
    2.Start the Streamlit App
        streamlit run app.py


## Model Details

* **Sentiment Analysis: Uses the transformers library with a pre-trained sentiment analysis model.
* **Text-to-Speech (TTS): Uses the gTTS library to convert text to Hindi speech.
* **Web Scraping: Uses BeautifulSoup4 and requests to extract news articles.
* **Topic Extraction: Uses KeyBERT to identify key topics in articles.

## API Development

* The application uses Flask (or FastAPI) to provide API endpoints.
* The main endpoint is `/news_report` (POST), which takes a JSON payload with the `company_name` and returns a JSON response containing the news report.
* To access the API (example):
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"company_name": "Tesla"}' http://your-api-endpoint/news_report
    ```

## API Usage

* No third-party paid APIs are used in this project.
* All models used in the transformers library are open source.


## Assumptions & Limitations

* Web scraping is dependent on the structure of the target websites. Changes to those websites can break the scraping functionality.
* Sentiment analysis models may not fully capture complex opinions or sarcasm.
* Hindi TTS output quality depends on gTTS, which may not always produce perfect pronunciation.
* Input validation is limited (Assumes valid company names).
* Error handling is implemented for basic cases but may need further refinement for production use.

## Improvements

* More robust web scraping with error handling and source diversity.
*


#   News Summarization and Text-to-Speech Application

This application extracts news articles, performs sentiment analysis, and generates a Hindi TTS output.

##  Project Setup
