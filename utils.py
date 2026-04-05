import time
from llm import analyze_review

def safe_analyze(text):
    for attempt in range(3):
        try:
            return analyze_review(text)
        except Exception as e:
            with open("logs.txt", "a") as f:
                f.write(f"Error: {str(e)}\n")
            time.sleep(2)
    
    return {
        "sentiment": "Unknown",
        "summary": "Failed",
        "score": "0"
    }