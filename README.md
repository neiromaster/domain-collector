# Domain Collector

This script allows you to extract unique domains visited when browsing a given URL in a browser. It uses Playwright to open a browser, allows user interaction, and then saves the visited domains to a file.

- [Русская документация](docs/README_ru.md)

## Features

-   Opens a URL in a browser.
-   Allows user interaction with the browser.
-   Extracts all unique domains visited during the browsing session.
-   Saves the list of unique domains to a text file.

## Usage

To use the script, you need to have `uv` installed.

1.  **Install uv:**

    Follow the instructions for your system at: https://docs.astral.sh/uv/getting-started/installation/
    
2.  **Install Playwright and Chromium:**

    ```bash
    uvx playwright install chromium
    ```

3.  **Run the script:**
    
    ```bash
    uvx domain-collector <URL>
    ```

    Replace `<URL>` with the URL you want to open in the browser. For example:

    ```bash
    uvx domain-collector https://ya.ru
    ```

    You can also provide a URL without the scheme (e.g., `ya.ru`), and the script will automatically add `https://`.
 
4.  **Interact with the browser:**

    The script will open a browser window. You can interact with the page as you normally would.

5.  **Close the browser:**

    After you are done browsing, press `Enter` in the terminal to close the browser and save the domains.

6.  **Output:**

    The script will save the unique domains to a file named `<domain>_domains.txt` (e.g., `ya_ru_domains.txt`) in the same directory where you ran the script. If the file already exists, new domains will be added to the existing list, avoiding duplicates.

## Example

```bash
uvx domain-collector https://www.wikipedia.org
```

This will open the Wikipedia homepage in a browser. After you interact with the page and close the browser, the script will save the visited domains to a file named `wikipedia_org_domains.txt`.

## Cleanup

To remove all artifacts, you can use the following commands:

```bash
uvx playwright uninstall --all
uv cache clean # Use with caution, this will remove all uv cache
```

## Dependencies

-   Python 3.7+
-   Playwright
-   argparse

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
