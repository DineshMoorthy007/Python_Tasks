import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def format_url(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    return url

def scrape_website_links(user_url):
    user_url = format_url(user_url)

    try:
        response = requests.get(user_url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')

        found = False
        print(f"\nLinks found on: {user_url}\n" + "-"*60)

        for link in links:
            text = link.get_text(strip=True)
            href = link.get('href')

            if not href or href.startswith(("javascript:", "mailto:")):
                continue

            absolute_url = urljoin(user_url, href)

            if text:
                print(f"• {text}\n  -> {absolute_url}")
            else:
                print(f"• (no text)\n  -> {absolute_url}")

            found = True

        if not found:
            print("No usable links found on the page.")

    except requests.exceptions.MissingSchema:
        print("Invalid URL format. Please include a domain.")
    except requests.exceptions.ConnectionError:
        print("Could not connect to the website.")
    except requests.RequestException as e:
        print("Request failed:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    url_input = input("Enter a website URL (e.g., python.org): ").strip()
    scrape_website_links(url_input)