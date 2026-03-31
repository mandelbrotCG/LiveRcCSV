from src.scraper import Scraper
from datetime import datetime, timedelta
from src.helpers import *
from pathlib import Path
import os

class CsvCreator:
    def __init__(self, root_dir, root_url, start_date, end_date=None):
        self.root_dir  = root_dir
        self.root_url  = root_url
        self.curr_date = datetime.strptime(start_date, DATE_FORMAT)
        self.end_date  = datetime.strptime(end_date, DATE_FORMAT) if end_date else datetime.now()

        if os.path.exists("visited_sites.txt"):
            with open("visited_sites.txt", "r") as f:
                self.visited = f.read().split("\n")
        else:
            self.visited = []
    
    def mark_as_visited(self, date_str):
        with open("visited_sites.txt", "a") as f:
            f.write(date_str + "\n")

    def create_csvs(self, racer_name):
        while self.curr_date <= self.end_date:
            date_str = self.curr_date.strftime(DATE_FORMAT)
            self.curr_date += timedelta(days=1)

            year_str, month_str, day_str = date_str.split("-")
            if date_str in self.visited: 
                print(f'Skipping {date_str}, marked as already processed')
                continue

            print(f' ------ Processing {date_str}')
            scraper = Scraper(self.root_url, racer_name)
            links = scraper.links_for_date(date_str)
            if len(links) == 0: 
                self.mark_as_visited(date_str)
                continue

            folder_path = f'{self.root_dir}/race_times/{racer_name}/{year_str}/{month_str}/{day_str}/'
            Path(folder_path).mkdir(parents=True, exist_ok=True)

            print(f'\tFound {len(links)} links')
            for link in links:
                lap_times = scraper.extract_lap_times(link)
                time_str  = str(scraper.get_race_time(link)).replace(":", "_")
                print(f'\tProcessing {time_str}')
                with open(folder_path + time_str + ".csv", "w") as f:
                    f.write("Lap Number,Lap Time\n")
                    for i in range(len(lap_times)):
                        f.write(f'{i+1},{lap_times[i]}\n')

            self.visited.append(date_str)
            self.mark_as_visited(date_str)

