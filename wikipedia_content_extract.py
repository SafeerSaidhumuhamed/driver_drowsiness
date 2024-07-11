import requests
from bs4 import BeautifulSoup

# List of Wikipedia URLs
urls = [
    "https://en.wikipedia.org/wiki/Artificial_intelligence",
    "https://en.wikipedia.org/wiki/Machine_learning",
    "https://en.wikipedia.org/wiki/Natural_language_processing",
    "https://en.wikipedia.org/wiki/Data_science",
    "https://en.wikipedia.org/wiki/Big_data",
    "https://en.wikipedia.org/wiki/Deep_learning",
    "https://en.wikipedia.org/wiki/Computer_vision",
    "https://en.wikipedia.org/wiki/Robotics",
    "https://en.wikipedia.org/wiki/Internet_of_things",
    "https://en.wikipedia.org/wiki/Cybersecurity",
    "https://en.wikipedia.org/wiki/Quantum_computing",
    "https://en.wikipedia.org/wiki/Bioinformatics",
    "https://en.wikipedia.org/wiki/Cryptography",
    "https://en.wikipedia.org/wiki/Blockchain",
    "https://en.wikipedia.org/wiki/Cloud_computing"
]

# Function to fetch and clean text from a URL
def fetch_long_text(url, min_word_count=100):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    long_paragraphs = [para.get_text() for para in paragraphs if len(para.get_text().split()) >= min_word_count]
    text = ' '.join(long_paragraphs)
    return text

# Fetch and combine long text from all URLs
combined_text = ""
for url in urls:
    combined_text += fetch_long_text(url) + "\n"

# Save the combined text to a file
with open("C:/Users/safee/Desktop/Dissertation/combined_text.txt", "w", encoding='utf-8') as file:
    file.write(combined_text)

print("Long texts fetched and saved successfully.")
