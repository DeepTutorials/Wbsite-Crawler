# Website Crawler

This Python script performs a internal web crawl starting from a given URL. It extracts and collects all internal links within the same domain up to a specified depth and saves them to a text file.

## Features

- Crawls a website up to a specified depth (default: 3 levels).
- Extracts all internal links from HTML anchor tags.
- Avoids revisiting the same URL.
- Respects polite crawling with configurable delay between requests.
- Saves the list of discovered URLs to a file (`found.txt`).

For Windows 64 bit
