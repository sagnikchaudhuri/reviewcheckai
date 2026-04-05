from bs4 import BeautifulSoup

def scrape_reviews(file_path="reviews.html"):
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    
    return [r.text.strip() for r in soup.select(".review")]