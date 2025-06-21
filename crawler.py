import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin, urlparse
import re

# Start URL
start_url = "https://example.com"
domain = "www.example.com"

# Set for previously visited URLs to avoid duplicates
visited_urls = set()
urls_to_visit = set([start_url])

# Headers to look like a normal browser
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def is_internal_url(url):
"""Checks whether a URL belongs to the same domain."""
parsed = urlparse(url)
return parsed.netloc == domain or parsed.netloc == ""

def crawl_website(max_depth=3, delay=2):
"""Crawls the website to a specified depth and with a delay between requests."""
depth = 0
while urls_to_visit and depth < max_depth:
current_urls = list(urls_to_visit)
urls_to_visit.clear()

for url in current_urls:
if url in visited_urls:
continue

print(f"Visits: {url}")
try:
response = requests.get(url, headers=headers, timeout=5)
if response.status_code == 200:
soup = BeautifulSoup(response.text, 'html.parser')

# Extract all links on the page
for link in soup.find_all('a', href=True):
href = link['href']
absolute_url = urljoin(url, href)

if is_internal_url(absolute_url) and absolute_url not in visited_urls:
urls_to_visit.add(absolute_url)

visited_urls.add(url)
else:
print(f"Error retrieving {url}: Status code {response.status_code}")
except Exception as e:
print(f"Error at {url}: {str(e)}")

# Delay to avoid overloading the server
time.sleep(delay)

depth += 1
print(f"Depth {depth} completed. URLs found: {len(visited_urls)}")

def save_urls_to_file(filename="found.txt"):
"""Saves all found URLs to a text file."""
try:
with open(filename, 'w', encoding='utf-8') as file:
file.write("Pages found on the website:\n\n")
for url in sorted(visited_urls):
file.write(f"{url}\n")
file.write(f"\nTotal number of pages found: {len(visited_urls)}\n")
print(f"All URLs were successfully saved to {filename}.")
except Exception as e:
print(f"Error saving URLs to {filename}: {str(e)}")

if __name__ == "__main__":
print("Starting crawling the website...")
crawl_website(max_depth=3, delay=2)

print("\nPages found on the website:")
for url in sorted(visited_urls):
print(url)
print(f"\nTotal number of pages found: {len(visited_urls)}")

# Save the URLs to a file
save_urls_to_file("found.txt")
