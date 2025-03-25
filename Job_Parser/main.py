import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

JOBS_FILE = "jobs.json"

def parse_jobs(city, category):

    if category == "it-administracja":
        cc = 5015
    elif category == "it-oprogramowania":
        cc = 5016
    elif category == "sprzedaż":
        cc = 5028
    else:
        cc = 5012

    """Парсит вакансии и сохраняет в JSON."""
    url = f"https://www.pracuj.pl/praca/{city};wp/{category};cc,{cc}?rd=30"
    
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(5)  # Даем время загрузиться

        soup = BeautifulSoup(driver.page_source, "html.parser")
        job_listings = soup.find_all("div", class_="tiles_cobg3mp")  # Подбери актуальный класс

        jobs = []
        for job in job_listings:
            title_tag = job.find("h2", class_="tiles_h1p4o5k6")
            link_tag = job.find("a", class_="tiles_cnb3rfy core_n194fgoq")

            if title_tag and link_tag:
                jobs.append({
                    "title": title_tag.text.strip(),
                    "url": link_tag.get("href")
                })

        with open(JOBS_FILE, "w", encoding="utf-8") as f:
            json.dump(jobs, f, indent=4, ensure_ascii=False)

        return jobs  # Вернем список вакансий

    finally:
        driver.quit()

if __name__ == "__main__":
    parse_jobs()
