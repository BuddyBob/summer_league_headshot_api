#!/usr/bin/env python3
import csv
import time
from pathlib import Path
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.filename_utils import clean_filename

class NBAImageScraper:
    def __init__(self, download_dir, csv_path):
        self.download_dir = Path(download_dir).expanduser()
        self.csv_path = csv_path
        self.session = requests.Session()
        self.download_dir.mkdir(parents=True, exist_ok=True)
        
    def _load_players(self):
        with open(self.csv_path, 'r') as f:
            return [row[1] for row in csv.reader(f) if len(row) >= 2 and row[0] != 'Team']

    def _get_player_image(self):
        try:
            elements = self.driver.find_elements(By.CSS_SELECTOR, 'img[src*="headshots"]')
            for element in elements:
                url = element.get_attribute('src')
                if url and 'headshots' in url:
                    return url
        except:
            pass
        return None
        
    def _download_image(self, url, filename):
        try:
            response = self.session.get(url, headers={'Referer': 'https://www.nba.com/'}, timeout=30)
            if response.status_code == 200:
                (self.download_dir / filename).write_bytes(response.content)
                return True
        except:
            pass
        return False
    
    def _search_player(self, player_name):
        try:
            search_input = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="__next"]/div[2]/div[2]/main/div[2]/section/div/div[1]/div[2]/div/input')))
            search_input.clear()
            search_input.send_keys(player_name)
            search_input.send_keys(Keys.ENTER)
            time.sleep(1)
            
            image_url = self._get_player_image()
            if image_url:
                filename = f"{clean_filename(player_name)}.png"
                return self._download_image(image_url, filename)
            return False
        except:
            return False
        
    def scrape(self):
        players = self._load_players()
        
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 15)
        
        try:
            self.driver.get("https://www.nba.com/players")
            time.sleep(3)
            
            successful = 0
            for player in players:
                if self._search_player(player):
                    successful += 1
                time.sleep(1)
                
            return successful, len(players)
            
        finally:
            if self.driver:
                self.driver.quit()

def main():
    scraper = NBAImageScraper('../NBA_Scraped_Headshots', '../NBA_Roster_Clean.csv')
    successful, total = scraper.scrape()
    print(f"Downloaded: {successful}/{total}")

if __name__ == "__main__":
    main()