import os
import re
import logging
from typing import List, Set
from urllib.parse import ParseResult, urlparse


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
