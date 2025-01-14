import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Check domains.")
    parser.add_argument(
        "domains",
        metavar="DOMAIN",
        type=str,
        nargs="+",
        help="Domain to check.",
    )
    args = parser.parse_args()
    print(f"Hello from check-domains! You passed these domains: {args.domains}")
