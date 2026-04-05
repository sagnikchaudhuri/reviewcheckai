import pandas as pd
from scraper import scrape_reviews
from processing import clean_text, parse_output
from utils import safe_analyze
import os
from datetime import datetime

def main():
    print(" ReviewCheck AI")
    print(" Processing reviews with LLM pipeline...\n")

    reviews = scrape_reviews()
    print(f" Found {len(reviews)} reviews\n")

    data = []

    for i, review in enumerate(reviews):
        print(f" Processing review {i+1}/{len(reviews)}")

        cleaned = clean_text(review)
        result = safe_analyze(cleaned)
        sentiment, summary, score = parse_output(result)

        data.append({
            "review": cleaned,
            "sentiment": sentiment,
            "score": score,
            "summary": summary,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    # Create output folder
    os.makedirs("output", exist_ok=True)

    df = pd.DataFrame(data)

    # Convert score to numeric
    df["score"] = pd.to_numeric(df["score"], errors="coerce")

    # Sort by score
    df = df.sort_values(by="score", ascending=False)

    # --- EXPORTS ---

    #  CSV 
    csv_path = "output/reviews.csv"
    df.to_csv(csv_path, index=False)

    #  Excel export
    excel_path = "output/reviews.xlsx"
    df.to_excel(excel_path, index=False)


    print("\n Export Complete:")
    print(f"→ CSV: {csv_path}")
    print(f"→ Excel: {excel_path}")

    print(f"\n Total reviews processed: {len(data)}")

    # Overall rating
    avg_score = df["score"].mean()
    print(f" Overall Product Score: {round(avg_score, 2)}/10")

    print("\nPreview:")
    print(df.head())

if __name__ == "__main__":
    main()