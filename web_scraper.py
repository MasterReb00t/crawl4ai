import asyncio
import os
import re
from crawl4ai import AdaptiveCrawler, AdaptiveConfig

async def main():
    # Create a directory to store the scraped data
    output_dir = 'scraped_data/infor' # Directory to save the scraped markdown files
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Configure the crawler for a deep crawl
    config = AdaptiveConfig(
        max_depth=5,  # The maximum depth of the crawl
        max_pages=50  # The maximum number of pages to crawl
    )

    # Initialize the crawler
    crawler = AdaptiveCrawler(config=config)

    # Scrape the website
    state = await crawler.digest(start_url='https://docs.infor.com/csi/2023.x/en-us/csbiolh/default.html?helpcontent=lsm1454144041228.html', query='print documentation') # Starting URL and query

    # Save the result to markdown files
    if state and state.knowledge_base:
        for result in state.knowledge_base:
            # Create a valid filename from the URL
            url = result.url
            filename = re.sub(r'^https?://', '', url)
            filename = re.sub(r'[/:?"<>|*]', '_', filename)
            if not filename.endswith('.md'):
                filename += '.md'

            filepath = os.path.join(output_dir, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(result.markdown.raw_markdown)
        print(f"Scraping complete. The content has been saved to {output_dir}")

if __name__ == "__main__":
    asyncio.run(main())