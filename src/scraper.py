from bs4 import BeautifulSoup
import requests

class Scraper:
    def __init__(self, root, racer_name):
        self.root       = root
        self.racer_name = racer_name.lower().strip()
        self.params     = ["p=session_list"]


    def links_for_date(self, date_str):
        soup = self.make_soup_request(f'{self.root}/practice/?{"&".join(self.params + ["d=" + date_str])}')
        links = []

        for anchor in soup.find_all('a'):
            if anchor.get_text(strip=True).lower() == self.racer_name:
                href = anchor.get('href')
                if href: links.append(href)

        return links

    def extract_lap_times(self, race_url):
        soup = self.make_soup_request(f'{self.root}{race_url}')
        laps_div = soup.find('div', class_="laps_list")

        if not laps_div:
            print(f"laps_list not found for {race_url}")
            return
    
        spans = laps_div.find_all('span')
        spans = [self.extract_time_from_span(span) for span in spans]
        return spans
    
    def extract_time_from_span(self, span):
        span_list = span.get_text().split(":")
        if len(span_list) != 2: 
            print(f"Cannot parse time: {span.get_text()}")
            return f"Cannot parse time: {span.get_text()}"
        span_parsed = span_list[-1].replace("*", "").strip()
        try:
            return float(span_parsed)
        except:
            print(f'Cannot parse time to float: {span_parsed}')
            return f'Cannot parse time to float: {span_parsed}'

    def get_race_time(self, race_url):
        soup = self.make_soup_request(f'{self.root}{race_url}')
        calendar_time = soup.find('h5').get_text().strip()
        return calendar_time
    
    def make_soup_request(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup
        except:
            print(f'Failed to make request for the following URL: {url}')
            return None

