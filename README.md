# Domain Collector

This script allows you to extract unique domains visited when browsing a given URL in a browser. It uses Playwright to open a browser, allows user interaction, and then saves the visited domains to a file.

## Features

-   Opens a URL in a browser using Playwright.
-   Allows user interaction with the browser.
-   Extracts all unique domains visited during the browsing session.
-   Saves the list of unique domains to a text file.
-   Appends new domains to an existing file, avoiding duplicates.
-   Generates a filename based on the URL.
-   Uses `argparse` to accept the URL as a command-line argument.

## Usage

To use the script, you need to have Python and Playwright installed.

1.  **Install Playwright:**

    ```bash
    pip install playwright
    playwright install
    ```

2.  **Run the script:**

    ```bash
    python -m src.domain_collector <URL>
    ```

    Replace `<URL>` with the URL you want to open in the browser. For example:

    ```bash
    python -m src.domain_collector https://www.example.com
    ```

    You can also provide a URL without the scheme (e.g., `www.example.com`), and the script will automatically add `https://`.

3.  **Interact with the browser:**

    The script will open a browser window. You can interact with the page as you normally would.

4.  **Close the browser:**

    After you are done browsing, press Enter in the terminal to close the browser and save the domains.

5.  **Output:**

    The script will save the unique domains to a file named `<domain>_domains.txt` (e.g., `example_com_domains.txt`) in the same directory where you ran the script. If the file already exists, new domains will be added to the existing list, avoiding duplicates.

## Example

```bash
python -m src.domain_collector https://www.wikipedia.org
```

This will open the Wikipedia homepage in a browser. After you interact with the page and close the browser, the script will save the visited domains to a file named `wikipedia_org_domains.txt`.

## Dependencies

-   Python 3.7+
-   Playwright
-   argparse

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
