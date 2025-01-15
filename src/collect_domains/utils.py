import argparse
from typing import List


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
