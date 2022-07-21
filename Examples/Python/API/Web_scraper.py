import requests
from bs4 import BeautifulSoup as bs


def main(url):
    page = requests.get(url)
    soup = bs(page.content, "html.parser")
    
    results = soup.find("div", id= "ResultsContainer")
    job_elements = results.find_all("div", class_ = "card-content")
    
    for job in job_elements:
        name = job.find("h2").text
        company = job.find("h3").text
        loc = job.find(class_="location").text.strip()

        print()
        print(name)
        print(company)
        print(loc)
        print()
        print("*"*10)

url = "https://realpython.github.io/fake-jobs/"
main(url)