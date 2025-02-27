import argparse
import asyncio
from typing import List
from urllib.parse import urlparse

from domain_collector.utils.browser import get_domains_from_browser
from domain_collector.utils.file_operations import (
    generate_filename,
    save_domains_to_file,
)


async def process_domains(target_url: str) -> None:
    visited_domains: List[str] = await get_domains_from_browser(target_url)
    filename: str = generate_filename(target_url)
    save_domains_to_file(visited_domains, filename)
    print(f"Visited domains saved to: {filename}")


def main():
    parser = argparse.ArgumentParser(description="Extract domains from a website.")
    parser.add_argument("url", help="The URL to open in the browser.")
    args = parser.parse_args()

    target_url: str = args.url
    if not urlparse(target_url).scheme:
        target_url = "https://" + target_url

    asyncio.run(process_domains(target_url))
