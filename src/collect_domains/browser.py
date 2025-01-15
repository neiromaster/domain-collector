import logging
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
