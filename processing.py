def clean_text(text):
    return text.replace("\n", " ").strip()

def parse_output(json_output):
    try:
        sentiment = json_output.get("sentiment", "Unknown")
        summary = json_output.get("summary", "N/A")
        score = json_output.get("score", "0")
        return sentiment, summary, score
    except:
        return "Unknown", "Parsing Failed", "0"