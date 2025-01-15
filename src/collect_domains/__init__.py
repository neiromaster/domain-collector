import argparse
import logging
import os
import re
from typing import List, Set
from urllib.parse import urlparse, ParseResult
from playwright.sync_api import sync_playwright


def get_domains_from_browser(url: str) -> List[str]:
    """
    Opens a URL in a browser using Playwright, allows user interaction, and returns a list of domains visited.

    Args:
        url (str): The URL to open.

    Returns:
        List[str]: A list of unique domains visited during the session.
    """
    logging.basicConfig(level=logging.INFO)
    domains: Set[str] = set()

    with sync_playwright() as p:
        try:
            browser = p.firefox.launch(headless=False)
            page = browser.new_page()

            def request_handler(request):
                parsed_url: ParseResult = urlparse(request.url)
                if parsed_url.netloc:
                    domains.add(parsed_url.netloc)

            page.on("request", request_handler)

            page.goto(url)
            logging.info(f"Opened URL: {url}")

            input("Press Enter to close the browser and get the domains...")

        except Exception as e:
            logging.error(f"An error occurred: {e}")
        finally:
            if "browser" in locals() and browser:
                browser.close()
                logging.info("Browser closed.")

    return list(domains)


def generate_filename(url: str) -> str:
    """Generates a filename from the URL."""
    parsed_url: ParseResult = urlparse(url)
    filename: str = parsed_url.netloc.replace("www.", "")
    filename = re.sub(r"[^a-zA-Z0-9]", "_", filename)
    return f"{filename}_domains.txt"


def save_domains_to_file(domains: List[str], filename: str) -> None:
    """Saves the list of unique domains to a file, sorted alphabetically."""
    try:
        existing_domains: Set[str] = set()
        if os.path.exists(filename):
            with open(filename, "r") as f:
                for line in f:
                    existing_domains.add(line.strip())

        unique_domains: List[str] = sorted(list(set(domains) | existing_domains))

        with open(filename, "w") as f:
            for domain in unique_domains:
                f.write(f"{domain}\n")
        logging.info(f"Unique domains saved to: {filename}")
    except Exception as e:
        logging.error(f"Error saving domains to file: {e}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract domains from a website.")
    parser.add_argument("url", help="The URL to open in the browser.")
    args = parser.parse_args()

    target_url: str = args.url
    if not urlparse(target_url).scheme:
        target_url = "https://" + target_url

    visited_domains: List[str] = get_domains_from_browser(target_url)
    filename: str = generate_filename(target_url)
    save_domains_to_file(visited_domains, filename)
    print(f"Visited domains saved to: {filename}")


if __name__ == "__main__":
    main()
