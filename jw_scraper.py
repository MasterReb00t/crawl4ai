import asyncio
import os
from crawl4ai import AdaptiveCrawler as Crawl4ai

async def main():
    # Create a directory to store the scraped data
    if not os.path.exists('scraped_data'):
        os.makedirs('scraped_data')

    # Initialize the crawler
    crawler = Crawl4ai()

    # Scrape the website
    state = await crawler.digest(start_url='https://www.jw.org', query='main page content')

    # Save the result to a markdown file
    if state and state.knowledge_base:
        with open('scraped_data/jw_org_homepage.md', 'w') as f:
            f.write(state.knowledge_base[0].markdown.raw_markdown)
        print("Scraping complete. The content has been saved to scraped_data/jw_org_homepage.md")

if __name__ == "__main__":
    asyncio.run(main())
