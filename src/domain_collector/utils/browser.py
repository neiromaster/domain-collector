import asyncio

from playwright.async_api import async_playwright
from urllib.parse import urlparse, ParseResult
from typing import List, Set
import logging


async def get_domains_from_browser(url: str) -> List[str]:
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

    async with async_playwright() as p:
        try:
            # Launch the browser in non-headless mode
            browser = await p.chromium.launch(headless=False)
            context = await browser.new_context(no_viewport=True)

            # Add request handler to existing pages and new pages
            def setup_request_interception(new_page):
                """
                Sets up request interception for a given page.
                """
                new_page.on("request", request_handler)

            # Intercept requests on new pages
            context.on("page", setup_request_interception)

            # Open the initial page
            page = await context.new_page()
            await page.goto(url)

            logging.info(f"Opened URL: {url}")

            # Create an event to wait for user input
            user_input_event = asyncio.Event()

            def on_user_input():
                """
                Callback function to set the event when Enter is pressed.
                """
                print("Press Enter to close the browser and get the domains...")
                input()  # Wait for Enter key press
                user_input_event.set()

            # Run the callback in a separate thread
            asyncio.get_running_loop().run_in_executor(None, on_user_input)

            # Wait for the event asynchronously
            await user_input_event.wait()

        except Exception as e:
            logging.error(f"An error occurred: {e}")
        finally:
            if "browser" in locals() and browser:
                await browser.close()
                logging.info("Browser closed.")

    return list(domains)
