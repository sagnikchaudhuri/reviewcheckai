
#  ReviewCheck AI- Review Intelligence System

##  Overview
ReviewSense AI is a Python-based application that extracts, processes, and analyzes product reviews using a Large Language Model (LLM) via an OpenAI-compatible API, Groq

The system performs sentiment analysis, assigns numerical scores, generates concise summaries, and aggregates insights into structured datasets for further analysis.

---

## Key Features

-  Review Extraction (HTML-based scraping)
-  LLM-Powered Sentiment Analysis (OpenAI-compatible API via Groq)
-  Numerical Sentiment Scoring (1–10 scale)
-  Automatic Summary Generation
-  Aggregated Product Rating
-  Retry Handling for API Failures
-  Logging for Debugging
-  Multi-Format Export:
  - CSV
  - Excel (.xlsx)
  

-

##  Tech Stack

- Python
- BeautifulSoup (Web Scraping)
- Pandas (Data Processing)
- OpenAI SDK (API Interface)
- Groq (OpenAI-Compatible LLM Endpoint)
- Llama 3.1 (LLM Model)

---

##  System Workflow

1. Extract reviews from HTML source  
2. Clean and preprocess text  
3. Send each review to LLM  
4. Receive structured JSON output:
   - Sentiment  
   - Score  
   - Summary  
5. Aggregate results  
6. Export to multiple formats  

##  Output Formats

- .csv
- .xlsx

## Setup

1. Add API key in `.env`:
   GROQ_API_KEY=your_key

2. Install dependencies:
   pip install -r requirements.txt

3. Run:
   python main.py

## Output
output/reviews.csv

## Design Decisions
- Used JSON output for robust parsing
- Implemented retry logic for API reliability
- Avoided direct scraping due to site restrictions

## Demo Video
Click on the link below
https://drive.google.com/drive/folders/1s90NkX4tIlVgeMA3RPzjeYdmz9nh4GGa?usp=sharing



