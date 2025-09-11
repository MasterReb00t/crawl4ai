# Crawl4AI Usage Summary

This document summarizes the steps taken to configure and use the `crawl4ai` library successfully.

## 1. Installation

To simplify the installation process, an installation script `install_crawl4ai.sh` is provided. This script automates the creation of a Python virtual environment and the installation of all necessary dependencies.

To use the script, run the following command in your terminal:

```bash
sh install_crawl4ai.sh
```

After the installation is complete, you need to activate the virtual environment to use `crawl4ai`:

```bash
source c4a_env/bin/activate
```

## 2. Basic Scraping: Single Page

Our first task was to scrape the homepage of `jw.org`. The script `jw_scraper.py` was created for this purpose. Here are the key steps that were involved:

- **Import `AdaptiveCrawler`:** We learned that `from crawl4ai import AdaptiveCrawler as Crawl4ai` is the correct way to import the main crawler class.
- **Use `async` and `await`:** The crawler's methods are asynchronous, so we need to use `async def main()` and `await` when calling crawler methods.
- **Use the `digest` method:** The `digest` method is used to start the crawling process. It requires a `start_url` and a `query`.
- **Save the output:** The scraped content is stored in the `state.knowledge_base`. We can access the markdown content of the first result with `state.knowledge_base[0].markdown.raw_markdown` and save it to a file.

## 3. Deep Crawl Scraping: Knowledge Base

To scrape an entire knowledge base like `https://docs.jan.ai/`, we created the `jan_ai_scraper.py` script. This script is similar to the basic scraper but includes a few key differences:

- **Configure `AdaptiveConfig`:** To perform a deep crawl, we need to configure the `AdaptiveCrawler` with a custom `AdaptiveConfig`. We can set `max_depth` and `max_pages` to control the extent of the crawl.
- **Iterate through the knowledge base:** For a deep crawl, the `state.knowledge_base` will contain multiple results. We can iterate through this list to access each scraped page.
- **Save multiple files:** We can generate a unique filename for each scraped page based on its URL and save each page as a separate markdown file.

## 4. Troubleshooting

During the process, we encountered and resolved a few issues:

- **`ModuleNotFoundError`:** We initially had `ModuleNotFoundError` for `pydantic` and `lark`. This was resolved by adding the missing dependencies to the `requirements.txt` file and reinstalling the dependencies using `pip install -r requirements.txt`.
- **`ImportError`:** We encountered an `ImportError` for `Crawl4ai`. By inspecting the `crawl4ai/__init__.py` file, we found that `AdaptiveCrawler` is the correct class to use.
- **`AttributeError`:** We received an `AttributeError` when trying to use the `run` method on the `AdaptiveCrawler` object. By examining the `adaptive_crawler.py` file, we discovered that `digest` is the correct method to use.
