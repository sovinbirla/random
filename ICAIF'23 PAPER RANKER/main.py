import asyncio
from bs4 import BeautifulSoup
import requests
from pyppeteer import launch
from lxml import html


def fetch_citations(title):
  # Construct the search URL based on the paper title
  search_url = f'https://dl.acm.org/action/doSearch?AllField={title.replace(" ", "+")}'

  # Send a GET request to the URL
  response = requests.get(search_url)

  # Parse the HTML content
  tree = html.fromstring(response.content)

  # Define the XPath expression
  xpath = '/html/body/div[3]/div/div[1]/main/div[1]/div/div[2]/div/ul/li[1]/div[2]/div[2]/div/div[3]/div/div[1]/ul/li[1]/div/ul/li[2]/span/span'

  # Find the element using XPath
  element = tree.xpath(xpath)
  print(element)
  citations = html.tostring(element[0], encoding='unicode')
  # Check if the element is found
  if element:
    print(int(citations))  # Print the HTML content of the element
  else:
    print("Element not found")
  return int(citations)


def fetch_paper_data(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  papers = []
  rows = soup.select(
      'div > main > article > div > div > div > figure > table > tbody > tr')

  # Iterate over the rows and print the text content of the first column
  for row in rows:
    first_column_text = row.find('td').get_text().strip()
    # print(first_column_text)
    papers.append(first_column_text)
  return papers


def main():
  url = "https://ai-finance.org/icaif-23-accepted-papers/"
  papers = fetch_paper_data(url)  # Extract top 10 papers
  paper_citations = {}
  for paper in papers:
    citations = fetch_citations(paper)
    paper_citations[paper] = citations

  print(paper_citations[:5])
  sorted_papers = sorted(paper_citations.items(),
                         key=lambda x: x[1],
                         reverse=True)
  print("Top 10 papers based on citations according to Google Scholar:")
  for i, (paper, citations) in enumerate(sorted_papers[:10], 1):
    print(f"{i}. {paper} - Citations: {citations}")


# asyncio.get_event_loop().run_until_complete(main())
main()
