from playwright.sync_api import sync_playwright
from urllib.parse import urlparse, ParseResult
from typing import List, Set
import logging

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

    def request_handler(request):
        """
        Handles network requests to extract domains.
        """
        parsed_url: ParseResult = urlparse(request.url)
        if parsed_url.netloc:
            domains.add(parsed_url.netloc)

    with sync_playwright() as p:
        try:
            # Launch the browser in non-headless mode
            browser = p.chromium.launch(headless=False)
            context = browser.new_context(no_viewport=True)

            # Add request handler to existing pages and new pages
            def setup_request_interception(page):
                """
                Sets up request interception for a given page.
                """
                page.on("request", request_handler)

            # Intercept requests on pages that already exist
            for page in context.pages:
                setup_request_interception(page)

            # Intercept requests on new pages
            context.on("page", setup_request_interception)

            # Open the initial page
            page = context.new_page()
            setup_request_interception(page)
            page.goto(url)

            logging.info(f"Opened URL: {url}")

            # Wait for user interaction
            input("Press Enter to close the browser and get the domains...")

        except Exception as e:
            logging.error(f"An error occurred: {e}")
        finally:
            if "browser" in locals() and browser:
                browser.close()
                logging.info("Browser closed.")

    return list(domains)
